echo "Running Production Application"
gunicorn -w 4 -b 0.0.0.0:8080 -t 180 --access-logfile - main:app

