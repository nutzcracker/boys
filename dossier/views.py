from django.shortcuts import render, get_object_or_404

from .models import Category, Dossier, Property

from django.views.generic.edit import CreateView

from .forms import DossierForm, PropertyForm

from django.urls import reverse_lazy



def index(request):	
	dossier_list = Dossier.objects.all()
	context = {
		'dossier_list': dossier_list,
	}
	return render(request, 'dossier/index.html', context)

def detail(request, dossier_id):
	dossier = get_object_or_404(Dossier, pk=dossier_id)
	category = Category.objects.filter(dossier__id=dossier.id)
	props = Property.objects.filter(dossier__id=dossier.id)
	return render(request, 'dossier/detail.html', {'dossier': dossier, 'props': props, 'category': category})

def category_detail(request, category_id):
	category = get_object_or_404(Category, pk=category_id)
	dossiers = Dossier.objects.filter(category__id=category_id)
	return render(request, 'dossier/category_detail.html', {'dossiers': dossiers, 'category': category})

def property_detail(request, property_id):
	prop = get_object_or_404(Property, pk=property_id)
	dossier = get_object_or_404(Dossier, property__id=property_id)
	return render(request, 'dossier/property.html', {'prop':prop, 'dossier':dossier})

class DossierCreateView(CreateView):
	template_name = 'dossier/create.html'
	form_class = DossierForm
	success_url = reverse_lazy('index')

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['categories'] = Category.objects.all()
	# 	return context
