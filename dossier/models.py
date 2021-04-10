from django.db import models

# Create your models here.

class Dossier(models.Model):
	name = models.CharField(max_length=100, verbose_name='Имя')
	photo = models.ImageField(upload_to='photos', blank=True, verbose_name='Фото')
	description = models.TextField(null=True, blank=True, verbose_name='Описание')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Кенты'
		verbose_name = 'Кент'
		ordering = ['name']

class Category(models.Model):
	cat_type = models.CharField(max_length=200, verbose_name='Категория граждан')
	dossier = models.ManyToManyField('Dossier', blank=True)

	def __str__(self):
		return self.cat_type

	class Meta:
		verbose_name_plural = 'Разряды кентов'
		verbose_name = 'Разряд кента'

class Property(models.Model):
	name = models.CharField(max_length=50, verbose_name='Название')
	photo = models.ImageField(upload_to='photos', blank=True, verbose_name='Фото')
	description = models.TextField(null=True, blank=True, verbose_name='Описание')
	dossier = models.ForeignKey('Dossier', null=True, on_delete=models.PROTECT, verbose_name='Досье')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Экипировка'
		verbose_name_plural = 'Экипировки'
		ordering = ['name']

def __init__(self, *args, **kwargs):
	super(Dossier, self).__init__(self, *args, **kwargs)
	self.name = kwargs['name']
