from django.shortcuts import render
from bookstore.models import Book
from .forms import OrderForm, OrderDeliveryForm
from .models import OrderNoDel, OrderDelivery


def purchase (request, name):
    form = OrderForm
    try:
        book = Book.objects.get(name=name)
    except Book.DoesNotExist:
        book = None
    content = {
        'book': book,
        'form': form,
    }
    return render(request, 'purchase/purchase.html', content)


def order_delivery_input (request, name):
    form = OrderDeliveryForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            product = Book.objects.get(name=name)
            order = form.save()
            if product.is_sale is True:
                order.price = (product.price * (100 - product.percent_sale))/100
            else:
                order.price = product.price
            order.product = product.name
            order.save()
            context = {'product': product,
                       'order': order}
            return render(request, 'purchase/success_purchase.html', context)


def purchase_delivery(request, name):
    form = OrderDeliveryForm
    book = Book.objects.get(name=name)
    content = {
        'book': book,
        'form': form,
    }

    return render(request, 'purchase/purchase_delivery.html', content)

def order_input (request, name):
    form = OrderForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            product = Book.objects.get(name=name)
            order = form.save()
            if product.is_sale is True:
                order.price = (product.price * (100 - product.percent_sale))/100
            else:
                order.price = product.price
            order.product = product.name
            order.save()
            context = {'product': product,
                       'order': order}
            return render(request, 'purchase/success_purchase.html', context)
