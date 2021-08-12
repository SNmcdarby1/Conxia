from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, service):
    return price * service_id