# Generated by Django 2.2.2 on 2019-07-07 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0030_auto_20190707_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='create_at',
            field=models.DateTimeField(auto_created=datetime.datetime(2019, 7, 7, 14, 39, 9, 267513)),
        ),
    ]
