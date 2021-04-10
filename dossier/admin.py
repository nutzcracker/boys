from django.contrib import admin

# Register your models here.
from .models import Dossier, Category, Property

admin.site.register(Dossier)
admin.site.register(Category)
admin.site.register(Property)