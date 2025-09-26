from django.shortcuts import render
from .models import Autor, Articulo, Comentario

def home(request):
    articulos = Articulo.objects.all()
    return render(request, 'revista/home.html', {'articulos': articulos})
