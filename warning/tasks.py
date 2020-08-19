from __future__ import absolute_import
from celery import shared_task

@shared_task
# 定义的定时任务函数
def auto_sc():
    print('sc test?')
    return 'halo'

# # name表示设置任务的名称，如果不填写，则默认使用函数名做为任务名
# 定义的两个异步函数
@shared_task(name="send_sms")
def send_sms():
    print("发送短信!!!")
    return "s"


@shared_task(name="send_sms2")
def send_sms2():
    print("发送短信任务2!!!")
    print("p")
    return "p"