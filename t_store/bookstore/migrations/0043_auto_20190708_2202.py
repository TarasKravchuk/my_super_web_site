# Generated by Django 2.2.2 on 2019-07-08 19:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0042_auto_20190707_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='create_at',
            field=models.DateTimeField(auto_created=datetime.datetime(2019, 7, 8, 22, 2, 15, 345137)),
        ),
    ]
