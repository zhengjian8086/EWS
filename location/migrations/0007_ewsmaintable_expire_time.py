# Generated by Django 3.1 on 2020-08-19 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_auto_20200819_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='ewsmaintable',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 17, 19, 9, 673838), verbose_name='到期时间'),
        ),
    ]
