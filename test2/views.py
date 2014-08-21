# encoding: utf8
from django.views.decorators.http import require_GET
from django.shortcuts import render

from test2.models import Product, Trademark, Category

def render_products(request, products):
	""" Хелпер: отрендерить список продуктов. """
	return render(request, "product_list.html", 
		{"products": products,
		 "categories": Category.objects.all()})

def product_list(request):
	""" Список всех товаров. """

	return render_products(request, Product.objects.all())

def products_by_category(request, category_slug):
	""" Список товаров определенной категории. """

	#category = get_object_or_404(Trademark, slug=category_slug)
	return render_products(reqeust, Product.objects.all()) #%TODO!!!

def products_test_case(request):
	""" Список товаров по тестовому запросу. """
	return render_products(request, Product.selection_task())


def trademark_details(request, slug):
	""" Запись марки товаров. """

	trademark = get_object_or_404(Trademark, slug=slug)

	return render(request, "trademark_details.html", 
		{"trademark": trademark})
