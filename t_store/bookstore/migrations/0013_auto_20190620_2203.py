# Generated by Django 2.2.2 on 2019-06-20 19:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0012_auto_20190617_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='create_at',
            field=models.DateTimeField(auto_created=datetime.datetime(2019, 6, 20, 22, 3, 41, 722752)),
        ),
    ]