import time
import datetime


def count_expire_time():
    d_value = datetime.timedelta(days=0, hours=2, minutes=0)
    return datetime.datetime.now() + d_value
