# Generated by Django 2.2.2 on 2019-07-07 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdelivery',
            name='prim_key',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ordernodel',
            name='prim_key',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
