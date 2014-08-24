# encoding: utf8
# Фильтры

from django import template

register = template.Library()

@register.filter(name='price')
def price(number):
	return (unicode(number) + u" \u20BD")