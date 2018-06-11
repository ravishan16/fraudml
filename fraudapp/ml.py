#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ML Program."""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import make_scorer
import xgboost as xg
from sklearn.model_selection import GridSearchCV
from random import randrange, uniform

def my_custom_loss_func(ground_truth, predictions):
    diff = np.abs(ground_truth - predictions).max()
    loss_value =  np.log(1 + diff)
    return loss_value


def preprocess(x):
    x['signup_time'] = pd.to_datetime(x['signup_time'])
    x['purchase_time'] = pd.to_datetime(x['purchase_time'])
    x['signup_week'] = x['signup_time'].dt.week
    x['signup_year'] = x['signup_time'].dt.year
    x['purchase_week'] = x['purchase_time'].dt.week
    x['purchase_year'] = x['purchase_time'].dt.year
    x['signup_to_purchase'] = (x['purchase_time'] - x['signup_time']).dt.days
    x['signup_time'] = (pd.to_datetime(x['signup_time']) - pd.to_datetime('1900-01-01')).dt.days
    x['purchase_time'] = (pd.to_datetime(x['purchase_time']) - pd.to_datetime('1900-01-01')).dt.days
    x['purchase_deviation'] = (x['purchase_value'] - x['purchase_value'].mean()) / x['purchase_value'].std()
    x = x.sort_values(by=['user_id', 'purchase_time'], ascending=True)

    return x

def train(cost):
    my_path = os.path.abspath(os.path.dirname(__file__))
    train_data_file = os.path.join(my_path,'fraud.csv')
    fraud_df = pd.read_csv(train_data_file)
    fraud_df = fraud_df.drop(columns=fraud_df.columns[0], axis=1)
    fraud_df = preprocess(fraud_df)
    features = ['signup_time', 'purchase_time', 'purchase_value',
                'device_id', 'source', 'browser', 'sex', 'age', 'ip_address',
                'signup_week', 'signup_year', 'purchase_week',
                'purchase_year', 'signup_to_purchase', 'purchase_deviation']
    le = LabelEncoder()
    for col in fraud_df.select_dtypes(include='object'):
        fraud_df[col] = le.fit_transform(fraud_df[col])
    train = fraud_df.sample(int(0.7 * len(fraud_df)))
    test = fraud_df[~fraud_df['user_id'].isin(train['user_id'])]

    your_param_grid = {  # ---- This is not an exhaustive list of parameters, it's small for speed
        'max_depth': [1, 3, 5],
        'min_child_weight': [1, 5],
        'learning_rate': [.1],
        'subsample': [0.8],
        'colsample_bytree': [0.8]
    }

    loss = make_scorer(my_custom_loss_func, greater_is_better=False)
    clf = xg.XGBClassifier()
    grid = GridSearchCV(clf, your_param_grid, cv=5, scoring=loss, n_jobs=2)
    grid.fit(train[features], train['class'])
    print("Best Parameters: ", grid.best_params_)
    clf = xg.XGBClassifier(**grid.best_params_)
    clf.fit(train[features], train['class'])
    top_features = ['ip_address', 'device_id', 'purchase_time', 'purchase_value', 'signup_time', 'age']
    clf = xg.XGBClassifier(**grid.best_params_)
    clf.fit(train[features], train['class'])
    # imp_df = pd.DataFrame(zip(features, clf.feature_importances_), columns=['feature', 'importance']).sort_values(
    #     'importance', ascending=False)
    # top_feature_df = imp_df.head(6)
    # top_features = list(top_feature_df.feature)
    clf = xg.XGBClassifier(**grid.best_params_)
    clf.fit(train[features], train['class'])
    predictions = clf.predict(test[features])
    # get accuracy metrics
    from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
    print(confusion_matrix(test['class'], predictions))
    print("Accuracy: " + str(accuracy_score(test['class'], predictions)))
    print("Precision: " + str(precision_score(test['class'], predictions)))
    print("Recall: " + str(recall_score(test['class'], predictions)))
    return accuracy_score(test['class'], predictions),precision_score(test['class'], predictions),recall_score(test['class'], predictions),uniform(0, 10)