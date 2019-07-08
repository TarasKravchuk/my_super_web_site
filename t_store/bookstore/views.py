from django.shortcuts import render
from .models import Genre, Book, Autors, Carousel, Review
from .forms import ReviewForm
from django.http import HttpResponseRedirect
# Create your views here.

def review (request, name):
    form = ReviewForm(request.POST)
    product = Book.objects.get(name=name)
    if request.user.is_authenticated and request.method == "POST" and form.is_valid():
        review = form.save()
        review.author = request.user.username
        review.save()
        review.book = product
        review.save()
        return product_page (request, name)


def start (request):
    carousel = Carousel.objects.all()
    context = {
               'carousel': carousel,
               }

    return render(request, 'starting_page.html', context)


def contact (request):
    return render(request, 'bookstore/contacts.html')

def bestsellers (request):
    ctx = {'books': Book.objects.all()}
    return render(request, 'bookstore/test_html.html', ctx)

def new_book (request):
    new_list = []
    for new_book in Book.objects.all():
        if new_book.new == True:
            new_list.append(new_book)
    content = {
        'books': new_list,
    }
    return render(request, 'bookstore/sale.html', content)


def product_page (request, name):
    form = ReviewForm(request.POST)
    book = Book.objects.get(name=name)
    review = Review.objects.all()
    content = {
       'book': book,
        'form': form,
        'review': review,
    }
    return render(request, 'bookstore/book-page.html', content)


def sale (request):
    sale_list = []
    for sale_book in Book.objects.all():
        if sale_book.is_sale == True:
            sale_list.append(sale_book)
    content = {
        'books': sale_list,
    }
    return render(request, 'bookstore/sale.html', content)

def languages (request):
    return render(request, 'bookstore/languages.html')

def genre (request):
    content = {'genres' : Genre.objects.all(),
               'books' : Book.objects.all(),
               }
    return render(request, 'bookstore/genre.html', content)

def all_book (request):

    content = {
        'books': Book.objects.all(),
              }
    return render(request, 'bookstore/all_books.html', content)

def about_us (request):
    return render(request, 'bookstore/about-us.html')