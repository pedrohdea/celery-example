from celery import Celery

app = Celery(
    broker='pyamqp://guest:guest@127.0.0.1:5672//'
)
app.add_defaults({'task_acks_late': True})
app.autodiscover_tasks(['example'], force=True)

