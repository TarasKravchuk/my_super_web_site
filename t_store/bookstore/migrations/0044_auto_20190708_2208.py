# Generated by Django 2.2.2 on 2019-07-08 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0043_auto_20190708_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='create_at',
            field=models.DateTimeField(auto_created=datetime.datetime(2019, 7, 8, 22, 8, 12, 708431)),
        ),
    ]