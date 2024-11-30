from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView

from .models import Libro
from applications.autor.models import Autor
# Create your views here.

class ListLibros(ListView):

    context_object_name = 'lista_libros'
    template_name = 'libro/listar.html'

    def get_queryset(self):

        palabra_clave = self.request.GET.get('kword','') 
        return Libro.objects.libros_autores(palabra_clave)

class Libros_genero(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/listar.html'

    def get_queryset(self):

        
        return Libro.objects.libros_genero()


    
        