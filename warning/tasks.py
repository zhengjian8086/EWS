from __future__ import absolute_import
from celery import shared_task


@shared_task()
def send_warning_mail(data_list):
    for item in data_list:
        with open("/mnt/d/Study/2020/EWS/tmp.log", "a") as f:
            f.write(str(item))
