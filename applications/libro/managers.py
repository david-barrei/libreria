from django.db import models
from django.db.models import Count
from django.db.models.functions import Lower

class LibroManager(models.Manager):

    def libros_autores(self,kword):

        resultado = self.filter(autor__id__icontains=kword)
        return resultado



    def libros_genero(self):

        resultado = self.values(
            'libro'
        ).annotate(
            num_prestamos= Count('libro'),
            
        )
        return resultado