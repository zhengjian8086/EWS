from __future__ import absolute_import

CELERY_BROKER_URL = 'redis://192.168.0.112:6379/1'
CELERY_RESULT_BACKEND = 'redis://192.168.0.112:6379/0'