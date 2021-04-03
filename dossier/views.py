from django.shortcuts import render, get_object_or_404

from .models import Dossier


def index(request):
    dossier_list = Dossier.objects.all()
    context = {
        'dossier_list': dossier_list,
    }
    return render(request, 'dossier/index.html', context)

def detail(request, dossier_id):
    dossier = get_object_or_404(Dossier, pk=dossier_id)
    return render(request, 'dossier/detail.html', {'dossier': dossier})
