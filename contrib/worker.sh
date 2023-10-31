# https://docs.celeryq.dev/en/stable/userguide/workers.html#starting-the-worker

celery -A celery_app worker -l info -c 4 -Q hello,matematica,mail