# Generated by Django 2.2.2 on 2019-07-07 20:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0040_auto_20190707_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='create_at',
            field=models.DateTimeField(auto_created=datetime.datetime(2019, 7, 7, 23, 42, 31, 202644)),
        ),
    ]