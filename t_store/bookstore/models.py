from django.db import models
from django.utils import timezone
import datetime

class Genre (models.Model):
    genre = models.CharField(max_length=120, verbose_name='genre')

    def __str__(self):
        return self.genre


class Autors(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='autor name')
    second_name = models.CharField(max_length=100, verbose_name='autor surname')

    def __str__(self):
        return self.first_name + ' ' + self.second_name

class Book(models.Model):
    name = models.CharField(max_length=300, unique=True)
    author = models.ManyToManyField(Autors)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='image_book', default='', blank=True, null=True)
    price = models.FloatField(verbose_name='Price')
    is_sale = models.BooleanField(default=False)
    percent_sale = models.FloatField(default=0.0)
    bestseller = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    book_genre = models.ManyToManyField(Genre)
    quantity = models.IntegerField(verbose_name='Quantity of books in the stock')
    pages = models.IntegerField(verbose_name='Quantity of pages')
    create_at = models.DateTimeField(auto_created=datetime.datetime.now())

    def __str__(self):
        return self.name

class Carousel (models.Model):
    name = models.CharField(max_length=80, unique=True)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='image_book',  blank=True, null=False)
    url = models.CharField(max_length=200)

    def __str__ (self):
        return self.name

class Review (models.Model):
    author = models.CharField(max_length=100, null=True)
    review = models.TextField(max_length=5000)
    time_review =  models.DateTimeField(default=timezone.now)
    book = models.ForeignKey(Book, on_delete='PROTECT', null=True)
