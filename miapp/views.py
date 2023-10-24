from django.shortcuts import render
from django.http import HttpResponse
from .models import Comunicado,Entidad

# Create your views here.

def index(request):
    title = "Inicio"

    comunicados = Comunicado.objects.all()
    total_c = Comunicado.objects.count()
    entidades = Entidad.objects.all()
    data = {
        "title": title,
        "comunicados":comunicados,
        "total_c":total_c,
        "entidades":entidades
    }
    return render(request,'miapp/index.html',data)

