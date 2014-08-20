# encoding: utf8

from django.db import models
from django.contrib import admin
from autoslug import AutoSlugField

from django_resized import ResizedImageField

class Trademark(models.Model):
	class Meta:
		verbose_name = u'Торговая марка'
		verbose_name_plural = u'Торговые марки'
		ordering = ['name']

	_max_width = _max_height = 150

	key = models.AutoField(primary_key=True)
	name = models.CharField(u'Наименование', max_length=200)
	image = ResizedImageField(u'Логотип', upload_to=".",
		max_width=_max_width, max_height = _max_height)
	description = models.TextField(u'Описание', max_length=300)
	phone_number = models.CharField(u'Телефон',max_length=12)
	email = models.EmailField(u'E-mail',max_length=30)
	site = models.URLField(u'Сайт',max_length=30)
	slug = AutoSlugField(populate_from='name')


	def __unicode__(self):
		return self.name

class Category(models.Model):
	class Meta:
		verbose_name = 'Категория товара'
		verbose_name_plural = 'Категории товаров'
		ordering = ['name']

	_max_height = _max_width = 100

	key = models.AutoField(primary_key=True)
	name = models.CharField(u'Наименование категории', max_length=250)
	image = ResizedImageField(u'Пиктограмма', upload_to=".", 
		max_width=_max_width, max_height = _max_height,
		blank = True) # Поле опционально: https://docs.djangoproject.com/en/dev/ref/models/fields/#null
	slug = AutoSlugField(populate_from='name')

	def __unicode__(self):
		return self.name

class Product(models.Model):
	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'
		ordering = ['name']

	_max_height = _max_width = 150
	image = ResizedImageField(u'Картинка', upload_to=".",
		max_width=_max_width, max_height = _max_height)


	key = models.AutoField(primary_key=True)
	name = models.CharField(u'Наименование', max_length=250)
	trademark = models.ForeignKey(Trademark)
	SKU = models.IntegerField(u'СКУ')
	description = models.CharField(u'Описание', max_length=300)
	price = models.DecimalField(u'Цена', max_digits=8, decimal_places=2)
	category = models.ForeignKey(Category)
	amount = models.IntegerField(u'Количество на складе')
	slug = AutoSlugField(populate_from='name')

	def __unicode__(self):
		return self.name

	def selection_task(self):
		""" Запрос для выдачи товаров определенной торговой марки (пр. «Phillips»), 
			принадлежащий нескольким категориям (пр. БЫТОВАЯ ТЕХНИКА, ОСВЕЩЕНИЕ, ТОВАРЫ ДЛЯ ДОМА) 
			и ценой, находящейся в определенных интервалах (пр. от 1000 и до 16000 р).

			Товар должен находиться на складе в количестве не менее 5 единиц. """ 

		return (Product.objects
			.filter(product_trademark="Philips")
			.filter(product_price__gte=1000)
			.filter(product_price__lte=16000)
			.filter(product_amount__gte=5))
	

admin.site.register(Category)
admin.site.register(Trademark)
admin.site.register(Product)