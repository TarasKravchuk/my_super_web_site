from django.contrib import admin
from django.urls import path
from . views import purchase_delivery, purchase, order_input, order_delivery_input

urlpatterns =[
    path('purchase/<str:name>', purchase, name='purchase/'),
    path('purchase-delivery/<str:name>', purchase_delivery,  name='purchase-delivery/'),
    path('order-input/<str:name>', order_input),
    path('order-delivery-input/<str:name>', order_delivery_input),
]
