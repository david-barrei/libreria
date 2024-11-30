from django.db import models
from django.db.models import Count
from django.db.models.functions import Lower

class LibroManager(models.Manager):

    def libros_autores(self,kword):

        resultado = self.filter(autor__id__icontains=kword)
        return resultado


    
    def listar_libros_genero(self,kword):#Filtrar libros por genero
        resultado = self.filter(
            genre__name__icontains = kword,
        )
        
        return resultado
   