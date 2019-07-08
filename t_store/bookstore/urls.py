from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.start, name='main'),
    path('contact-information', views.contact, name='contact-information/'),
    path('about-us', views.about_us, name='about-us/'),
    path('all-book', views.bestsellers, name='all-book/'),
    path('book-genre', views.genre, name='book-genre/'),
    path('new-book', views.new_book, name='new-book/'),
    path('book-sale', views.sale, name='book-sale/'),
    path('book-genre', views.genre, name='book-genre/'),
    path('book/<str:name>', views.product_page, name='book_detail'),
    path('book/review/<str:name>', views.review),

]
