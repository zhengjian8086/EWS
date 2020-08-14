from celery import Celery

app = Celery('demo',
             broker='amqp://guest@127.0.0.1//',
             backend='redis://@127.0.0.1:6379/2',
             )


# 创建任务函数
@app.task
def task_test():
    print("task is running")
