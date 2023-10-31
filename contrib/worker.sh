# https://docs.celeryq.dev/en/stable/userguide/workers.html#starting-the-worker
# Com virtualenv

# celery -A celery_app worker -l info --pool=solo -Q hello,matematica,mail

celery -A celery_app worker -l info -c 4 -Q hello,matematica,mail