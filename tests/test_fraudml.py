#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test for fraudml."""

from flask_testing import TestCase
import config
from fraudapp import create_app,model
import json

class TestFraudApp(TestCase):
    """TestFlaskApp class."""

    def create_app(self):
        return create_app(config,testing=True)

    def setUp(self):
        self.client = self.app.test_client()
        self.app.testing = True
        self.app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///tmp.db')
        model._create_database(SQLALCHEMY_DATABASE_URI='sqlite:///tmp.db')

    def tearDown(self):
        """ Test Suite Tear down."""
        model._drop_database(SQLALCHEMY_DATABASE_URI='sqlite:///tmp.db')
        pass

    def test_list(self):
        """Test Experiment List ."""
        result = self.client.get('/')
        assert result.status_code == 302

    def test_trend(self):
        """Test Trend ."""
        result = self.client.post('fraud/trend')
        assert result.status_code == 302


