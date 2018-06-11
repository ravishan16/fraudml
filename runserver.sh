echo "Running Production Application"
gunicorn -w 2 -b 0.0.0.0:8080 -t 180 --thread 2 --access-logfile - main:app

