from django import template

def currency_real(value):
    return f"R$ {value}"

register = template.Library()

register.filter("currency_real", currency_real)