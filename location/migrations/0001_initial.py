# Generated by Django 2.2.12 on 2020-08-08 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EWSMainTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SN', models.CharField(max_length=10, verbose_name='服务码')),
                ('modelName', models.CharField(max_length=30, verbose_name='服务码')),
                ('MAC', models.CharField(max_length=20, verbose_name='MAC')),
                ('line', models.CharField(max_length=10, verbose_name='线号')),
                ('row', models.CharField(max_length=10, verbose_name='杠号')),
                ('number', models.CharField(max_length=10, verbose_name='编号')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='入站时间')),
            ],
            options={
                'verbose_name_plural': 'EWS主表',
                'db_table': 'EWS',
            },
        ),
    ]
