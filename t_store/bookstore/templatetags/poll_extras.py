from django import template
register = template.Library()

@register.filter(name='new_price')
def new_price(price, percent):
    sale_price = price * (1-percent/100)
    return sale_price
