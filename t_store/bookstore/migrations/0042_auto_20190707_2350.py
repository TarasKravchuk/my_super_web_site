# Generated by Django 2.2.2 on 2019-07-07 20:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0041_auto_20190707_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='create_at',
            field=models.DateTimeField(auto_created=datetime.datetime(2019, 7, 7, 23, 50, 42, 337748)),
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
