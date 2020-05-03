
# Django
from django import template

register = template.Library()


@register.simple_tag
def volando_number():
    return '529511302570'


@register.simple_tag
def volar_number():
    return '529511727426'
