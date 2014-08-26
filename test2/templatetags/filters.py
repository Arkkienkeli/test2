# encoding: utf8
# Фильтры

from django import template
from django.utils.safestring import mark_safe


register = template.Library()

@register.filter(name='price')
def price(number):
	return (mark_safe(str(number) + ' <i class="fa fa-rub"></i>') )