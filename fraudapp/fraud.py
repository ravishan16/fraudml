#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""fraud blueprint."""

from fraudapp import get_model
from flask import Blueprint, redirect, render_template, request, url_for
from . import ml
import logging
import pandas as pd
fraud = Blueprint('fraud', __name__)


# [START list]
@fraud.route("/")
def list():
    token = request.args.get('page_token', None)
    message = request.args.get('message')
    experiments, next_page_token = get_model().list(cursor=token)

    return render_template(
        "list.html",
        experiments=experiments,
        next_page_token=next_page_token)
# [END list]


@fraud.route('/train', methods=['GET', 'POST'])
def train():
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        cost = data.get('cost')
        experiment = get_model().find(cost)
        if experiment:
            message = 'Model Trained Already for the Cost of a false positive  {}'.format(cost)
        else:
            accuracy,precision,recall,recall_dollars  = ml.train(cost)
            data['accuracy'] = accuracy
            data['precision'] = precision
            data['recall'] = recall
            data['recall_dollars'] = recall_dollars
            experiment = get_model().create(data)
            message = 'Model Trained Successfully for Cost {}'.format(cost)

        print (message)

        return redirect(url_for('.list', message = message))

    return render_template("train.html", action="Train", experiment={})
# [END add]

@fraud.route('/<id>/delete')
def delete(id):
    get_model().delete(id)
    message = 'Deleted Experiment ID {} Successfully'.format(id)
    return redirect(url_for('.list', message = message))


@fraud.route("/trend")
def chart():
    experiments = get_model().trend()
    # logging.info(experiments)
    df = pd.DataFrame(experiments)
    # logging.info(df)
    legend = 'Cost of False Positive (X) vs Recall Dollars (Y)'
    labels = df['cost']
    values = df['recall_dollars']
    return render_template('chart.html', values=values, labels=labels, legend=legend)
