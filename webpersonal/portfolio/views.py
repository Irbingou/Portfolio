from django.shortcuts import render
from .models import Project

# Create your views here.


def portfolio(request):
    # se define una variable para recuperar la
    # lista de proyectos guardada en el modelo Projects
    project = Project.objects.all()
    # para pasar datos a un template, se utliza un parametro 
    # conocido como diccionario de contexto y se asigna un nombre
    # para cada variable que se va a enviar al template
    return render(request, "portfolio/portfolio.html", {'projects': project})
