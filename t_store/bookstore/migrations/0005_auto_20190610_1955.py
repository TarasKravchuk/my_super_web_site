# Generated by Django 2.2.2 on 2019-06-10 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_auto_20190610_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='create_at',
            field=models.DateTimeField(auto_created=datetime.datetime(2019, 6, 10, 19, 55, 37, 810400)),
        ),
    ]
