#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""setup for flaskapp."""

from setuptools import setup

setup(
    name='fraudapp',
    version='0.0.1',
    url='https://github.com/ravishan16/fraudml',
    license='MIT',
    author='Ravishankar Sivasubramaniam',
    author_email='contact@ravishankars.com',
    description='Fraud Detection Machine Learning Flask App',
    packages=['fraudapp'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'SQLAlchemy>=1.1.6',
        'Flask-SQLAlchemy>=2.2',
        'pylint',
        'nose',
        'flask_testing',
        'coverage>=4.0,<4.4'
        'xgboost',
        'sklearn',
        'pandas',
        'numpy'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
