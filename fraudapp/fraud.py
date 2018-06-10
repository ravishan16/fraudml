#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""fraud blueprint."""

from fraudapp import get_model
from flask import Blueprint, redirect, render_template, request, url_for
from . import ml

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
        print (data)
        print (data['lossvalue'])
        lossvalue = data.get('lossvalue')
        experiment = get_model().find(lossvalue)
        if experiment:
            message = 'Model Trained Already for the Loss Value {}'.format(lossvalue)
        else:
            accuracy,precision,recall  = ml.train(lossvalue)
            data['accuracy'] = accuracy
            data['precision'] = precision
            data['recall'] = recall
            experiment = get_model().create(data)
            message = 'Model Trained Successfully'

        print (message)

        return redirect(url_for('.list', message = message))

    return render_template("train.html", action="Train", experiment={})
# [END add]

@fraud.route('/<id>/delete')
def delete(id):
    get_model().delete(id)
    message = 'Deleted Experiment ID {} Successfully'.format(id)
    return redirect(url_for('.list', message = message))
