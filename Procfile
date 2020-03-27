web: gunicorn app:app
worker: celery worker -A linkworker.app -l INFO --concurrency=18