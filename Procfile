web: gunicorn app:app
worker1: celery worker -A linkworker.app -l INFO --concurrency=4
worker2: celery worker -A linkworker.app -l INFO --concurrency=4
worker3: celery worker -A linkworker.app -l INFO --concurrency=4
worker4: celery worker -A linkworker.app -l INFO --concurrency=4