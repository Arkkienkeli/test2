#coding=utf-8

from django.db import models
from django.contrib import admin
from autoslug import AutoSlugField

class Trademark(models.Model):
	class Meta:
		verbose_name = 'Торговая марка'
		verbose_name_plural = 'Торговые марки'
		ordering = ['trademark_name']
	trademark_name = models.CharField(u'Наименование', max_length=200)
	trademark_logo = models.ImageField(u'Логотип', upload_to='logos/', height_field=150, width_field=150)
	trademark_description = models.CharField(u'Описание', max_length=300)
	trademark_phone_number = models.CharField(u'Телефон',max_length=12)
	trademark_email = models.CharField(u'E-mail',max_length=30)
	trademark_site = models.CharField(u'Сайт',max_length=30)
	trademark_slug = AutoSlugField(populate_from='trademark_name')

	def __unicode__(self):
		return self.title

class Category(models.Model):
	class Meta:
		verbose_name = 'Категория товара'
		verbose_name_plural = 'Категории товаров'
		ordering = ['category_name']
	category_name = models.CharField(u'Наименование категории', max_length=250)
	category_pic = models.ImageField(u'Пиктограмма', upload_to='pics/', height_field=100, width_field=100)
	category_slug = AutoSlugField(populate_from='category_name')

	def __unicode__(self):
		return self.title

class Product(models.Model):
	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'
		ordering = ['product_name']
	product_name = models.CharField(u'Наименование', max_length=250)
	product_trademark = models.ForeignKey(Trademark)
	product_SKU = models.IntegerField(u'СКУ')
	product_description = models.CharField(u'Описание', max_length=300)
	product_price = models.DecimalField(u'Цена', max_digits=8, decimal_places=2)
	product_category = models.ForeignKey(Category)
	product_amount = models.IntegerField(u'Количество на складе')
	product_slug = AutoSlugField(populate_from='product_name')

	def __unicode__(self):
		return self.title

admin.site.register(Category)
admin.site.register(Trademark)
admin.site.register(Product)

#q = Product.objects.filter(product_trademark="Philips").filter(product_price__gte 1000).filter
#(product_price__lte 16000).filter(product_amount__gte 4)
