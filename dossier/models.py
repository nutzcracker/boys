from django.db import models

# Create your models here.

class Dossier(models.Model):
	name = models.CharField(max_length=100, verbose_name='Имя')
	photo = models.ImageField(upload_to='photos', blank=True, verbose_name='Фото')
	description = models.TextField(null=True, blank=True, verbose_name='Описание')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Объект'
		verbose_name = 'Объект'
		ordering = ['name']

class Category(models.Model):
	cat_type = models.CharField(max_length=200, verbose_name='Класс объекта')
	dossier = models.ManyToManyField('Dossier', blank=True)

	def __str__(self):
		return self.cat_type

	class Meta:
		verbose_name_plural = 'Класс объекта'
		verbose_name = 'Класс объекта'

class Property(models.Model):
	name = models.CharField(max_length=50, verbose_name='Название')
	photo = models.ImageField(upload_to='photos', blank=True, verbose_name='Фото')
	description = models.TextField(null=True, blank=True, verbose_name='Описание')
	dossier = models.ForeignKey('Dossier', null=True, on_delete=models.PROTECT, verbose_name='Досье')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Снаряжение'
		verbose_name_plural = 'Снаряжения'
		ordering = ['name']

def __init__(self, *args, **kwargs):
	super(Dossier, self).__init__(self, *args, **kwargs)
	self.name = kwargs['name']
