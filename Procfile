web: gunicorn app:app
worker: celery worker -A linkworker.app -l INFO --concurrency=4 -n worker1
worker: celery worker -A linkworker.app -l INFO --concurrency=4 -n worker2
worker: celery worker -A linkworker.app -l INFO --concurrency=4 -n worker3
worker: celery worker -A linkworker.app -l INFO --concurrency=4 -n worker4