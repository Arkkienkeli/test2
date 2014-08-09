#coding=utf-8

from django.db import models
from django.contrib import admin

class Trademark(models.Model):
	class Meta:
		verbose_name = 'Торговая марка'
		verbose_name_plural = 'Торговые марки'
	trademark_title = models.CharField(u'Наименование', max_length=200)
	#logo = 
	trademark_description = models.CharField(u'Описание', max_length=300)
	trademark_phone_number = models.CharField(u'Телефон',max_length=12)
	trademark_email = models.CharField(u'E-mail',max_length=30)
	trademark_site = models.CharField(u'Сайт',max_length=30)
	def __unicode__(self):
		return self.title

class Category(models.Model):
	class Meta:
		verbose_name = 'Категория товара'
		verbose_name_plural = 'Категории товаров'
	category_name = models.CharField(u'Наименование категории', max_length=250)
	#category_pic = 


	def __unicode__(self):
		return self.title

class Product(models.Model):
	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'
	product_name = models.CharField(u'Наименование', max_length=250)
	product_trademark = models.ForeignKey(Trademark)
	#product_SKU = 
	product_description = models.CharField(u'Описание', max_length=300)
	product_price = models.DecimalField(u'Цена', max_digits=8, decimal_places=2)
	product_category = models.ForeignKey(Category)
	product_amount = models.IntegerField(u'Количество на складе')

	def __unicode__(self):
		return self.title

admin.site.register(Category)
admin.site.register(Trademark)
admin.site.register(Product)