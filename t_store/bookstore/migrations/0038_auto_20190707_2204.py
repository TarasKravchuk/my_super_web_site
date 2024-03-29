# Generated by Django 2.2.2 on 2019-07-07 19:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0037_auto_20190707_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='create_at',
            field=models.DateTimeField(auto_created=datetime.datetime(2019, 7, 7, 22, 4, 28, 190432)),
        ),
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(max_length=5000, verbose_name='Your review'),
        ),
        migrations.AlterField(
            model_name='review',
            name='time_review',
            field=models.DateTimeField(auto_created=datetime.datetime(2019, 7, 7, 22, 4, 28, 194656), null=True),
        ),
    ]
