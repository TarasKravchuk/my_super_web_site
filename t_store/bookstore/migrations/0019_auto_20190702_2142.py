# Generated by Django 2.2.2 on 2019-07-02 18:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0018_auto_20190702_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='create_at',
            field=models.DateTimeField(auto_created=datetime.datetime(2019, 7, 2, 21, 42, 22, 812646)),
        ),
    ]
