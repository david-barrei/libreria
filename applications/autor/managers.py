from django.db import models
from django.db.models import Count

class LibroManager(models.Manager):


    def listar_genero_libros(self):#Conteo de cuantos libros 
        resultado = self.annotate(
            num_libros= Count('libro_genero')
        )
        
        return resultado


    def autores_pais(self,kword):
        resultado = self.filter(country__iexact=kword)
        return resultado