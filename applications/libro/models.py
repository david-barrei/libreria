from django.db import models
from applications.autor.models import Autor, Genero
from .managers import *
# Create your models here.

class Libro(models.Model):
    title = models.CharField( max_length=50)
    publication = models.DateField(blank=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genero, on_delete=models.CASCADE)
    synopsis = models.CharField(max_length=100)

    objects = LibroManager()
    
    def __str__(self):
        return self.title 
    


