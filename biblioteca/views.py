from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Libro

def inicio(request):
    return HttpResponse("Hola, soy tu biblioteca!")

def resumen(request):
    total=Libro.objects.count()
    return HttpResponse(f"Actualmente hay {total} Libros registrados en la biblioteca.")
