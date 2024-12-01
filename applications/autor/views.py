from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from .models import Genero, Autor

# Create your views here.

class Libros_genero(ListView):
    context_object_name = 'generos'
    template_name = 'genero/listar.html'

    def get_queryset(self):

         
        return Genero.objects.listar_genero_libros()
    
class Autores_pais(ListView):
    context_object_name = 'autores'
    template_name = 'autor/listar.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')

        return Autor.objects.autores_pais(palabra_clave)