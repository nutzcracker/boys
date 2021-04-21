from django.forms import ModelForm

from .models import Dossier, Property

class DossierForm(ModelForm):
	class Meta:
		model = Dossier
		enctype="multipart/form-data"
		fields = ('name', 'description', 'photo')

class PropertyForm(ModelForm):
	class Meta:
		model = Property
		fields = ('name', 'photo', 'description', 'dossier')