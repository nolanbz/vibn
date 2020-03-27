web: gunicorn app:app
worker1: celery worker -A linkworker.app -l INFO --concurrency=4 -n worker1
worker2: celery worker -A linkworker.app -l INFO --concurrency=4 -n worker2
worker3: celery worker -A linkworker.app -l INFO --concurrency=4 -n worker3
worker4: celery worker -A linkworker.app -l INFO --concurrency=4 -n worker4