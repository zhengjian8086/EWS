# Generated by Django 2.2.12 on 2020-08-10 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ewsmaintable',
            name='area',
            field=models.CharField(max_length=10, null=True, verbose_name='区域'),
        ),
    ]
