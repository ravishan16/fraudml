#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Main Module."""
import fraudapp
import config


app = fraudapp.create_app(config)


# This is only used when running locally. When running live, gunicorn runs
# the application.
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)