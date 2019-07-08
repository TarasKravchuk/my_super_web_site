# Generated by Django 2.2.2 on 2019-06-08 20:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='name')),
                ('second_name', models.CharField(max_length=100, verbose_name='surname')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=120, verbose_name='genre')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=datetime.datetime(2019, 6, 8, 23, 9, 34, 757084))),
                ('name', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='image_book')),
                ('price', models.FloatField(verbose_name='Price')),
                ('is_sale', models.BooleanField(default=False)),
                ('percent_sale', models.FloatField(default=0.0)),
                ('bestseller', models.BooleanField(default=False)),
                ('new', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(verbose_name='Quantity of books in the stock')),
                ('pages', models.IntegerField(verbose_name='Quantity of pages')),
                ('author', models.ManyToManyField(to='bookstore.Autors')),
                ('genre', models.ManyToManyField(to='bookstore.Genre')),
            ],
        ),
    ]