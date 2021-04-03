from django.db import models

# Create your models here.

class Dossier(models.Model):
	name = models.CharField(max_length=100)
	photo = models.ImageField(upload_to='photos', blank=True)

class Category(models.Model):
	dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE)
	cat_type = models.CharField(max_length=200)


def __init__(self, *args, **kwargs):
	super(Dossier, self).__init__(self, *args, **kwargs)
	self.name = kwargs['name']
