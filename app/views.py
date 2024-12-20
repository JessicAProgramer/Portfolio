from django.shortcuts import render, get_object_or_404
from .models import Folio

def inicio(request):
    return render(request, 'inicio.html')

def sobre_mi(request):
    return render(request, 'sobre_mi.html')

def projectos(request):
    projects = Folio.objects.all()
    return render(request, 'projectos.html',{
        'projects': projects
    })

    