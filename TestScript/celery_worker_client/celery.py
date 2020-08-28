from __future__ import absolute_import
from celery import Celery

app = Celery('EWS_Celery')
app.config_from_object('celery_worker_client.config', namespace='CELERY')
app.autodiscover_tasks()