from django.forms import ModelForm
from .models import OrderDelivery, OrderNoDel

class OrderDeliveryForm(ModelForm):
    class Meta:
        model = OrderDelivery
        fields = ['payment_type', 'name', 'surname', 'mobile_phone', 'email', 'adres', 'date', 'time']


class OrderForm(ModelForm):
    class Meta:
        model = OrderNoDel
        fields = ['payment_type', 'name', 'surname', 'mobile_phone', 'email']
