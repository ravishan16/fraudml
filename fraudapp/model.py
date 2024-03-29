#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""DB Model."""

from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd

builtin_list = list

db = SQLAlchemy()


def init_app(app):
    db.init_app(app)


def from_sql(row):
    """Translates a SQLAlchemy model instance into a dictionary"""
    data = row.__dict__.copy()
    data['id'] = row.id
    data.pop('_sa_instance_state')
    return data



# [Experiment model]
class Experiment(db.Model):
    __tablename__ = 'experiments_t'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    cost = db.Column(db.Integer, unique=True)
    accuracy = db.Column(db.Float)
    precision = db.Column(db.Float)
    recall= db.Column(db.Float)
    recall_dollars= db.Column(db.Float)
    createdDate = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Experiment {0} - {1}>".format(self.id,self.first_name)
# [Experiment model]

def list(limit=10, cursor=None):
    cursor = int(cursor) if cursor else 0
    query = (Experiment.query
             .order_by(Experiment.id.desc())
             .limit(limit)
             .offset(cursor))
    experiment = builtin_list(map(from_sql, query.all()))
    next_page = cursor + limit if len(experiment) == limit else None
    return (experiment, next_page)


def trend():
    query = (Experiment.query
             .order_by(Experiment.cost.asc()))
    experiment = builtin_list(map(from_sql, query.all()))
    return experiment

# [START create]
def create(data):
    experiment = Experiment(**data)
    db.session.add(experiment)
    db.session.commit()
    return from_sql(experiment)
# [END create]

def find(cost):

    experiment = Experiment.query.filter_by(cost=cost).first()
    if not experiment:
        return None
    return from_sql(experiment)
# [END create]

def delete(id):
    Experiment.query.filter_by(id=id).delete()
    db.session.commit()


def _create_database(SQLALCHEMY_DATABASE_URI=None):
    """
    If this script is run directly, create all the tables necessary to run the
    application.
    """
    app = Flask(__name__)
    if SQLALCHEMY_DATABASE_URI:
        app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    else:
        app.config.from_pyfile('../config.py')
    init_app(app)
    with app.app_context():
        db.create_all()
    print("All tables created")

def _drop_database(SQLALCHEMY_DATABASE_URI=None):
    """
    If this script is run directly, create all the tables necessary to run the
    application.
    """
    app = Flask(__name__)
    if SQLALCHEMY_DATABASE_URI:
        app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    else:
        app.config.from_pyfile('../config.py')
    init_app(app)
    with app.app_context():
        db.drop_all()
    print("All tables created")

if __name__ == '__main__':
    _create_database()