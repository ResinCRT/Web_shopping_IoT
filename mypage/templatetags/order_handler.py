from django import template

register = template.Library()

@register.filter
def get_order_total(group):
    total = 0
    for item in group:
        total += item.quantity * item.product.price
    return total


