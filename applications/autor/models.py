from django.db import models
from .managers import LibroManager
# Create your models here.

class Autor(models.Model):
    first_name = models.CharField( max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField( blank=True, null=True)
    country = models.CharField( max_length=50)

    def __str__(self):
        return self.first_name +'-'+ self.last_name
    
class Genero(models.Model):
    name = models.CharField( max_length=20)

    objects = LibroManager()
    def __str__(self):
        return self.name 
    