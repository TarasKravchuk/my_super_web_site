from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Book)
admin.site.register(models.Autors)
admin.site.register(models.Genre)
admin.site.register(models.Carousel)
admin.site.register(models.Review)
