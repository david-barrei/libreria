
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView

from .models import Libro
from .models import Genero
from applications.autor.models import Autor
# Create your views here.

class ListLibros(ListView):

    context_object_name = 'lista_libros'
    template_name = 'libro/listar.html'

    def get_queryset(self):

        palabra_clave = self.request.GET.get('kword','') 
        return Libro.objects.libros_autores(palabra_clave)


class Genero_libro(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/listar.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')

        return Libro.objects.listar_libros_genero(palabra_clave)

    
        