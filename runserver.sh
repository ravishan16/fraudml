#!/bin/sh
set -e

echo "Running Production Application"
exec gunicorn -w 4 -b 0.0.0.0:8080 --access-logfile - main:app

