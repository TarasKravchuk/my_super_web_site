# Generated by Django 2.2.2 on 2019-07-07 20:41

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0039_auto_20190707_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='create_at',
            field=models.DateTimeField(auto_created=datetime.datetime(2019, 7, 7, 23, 41, 31, 100931)),
        ),
        migrations.AlterField(
            model_name='review',
            name='time_review',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
