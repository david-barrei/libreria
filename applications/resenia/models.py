from django.db import models
from .managers import ReseniaManager
from applications.libro.models import Libro
from django.core.exceptions import ValidationError
# Create your models here.

class Resenia(models.Model):
    book = models.ForeignKey(Libro, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    review_text = models.CharField(max_length=50)
    created_at = models.DateField( auto_now=False, auto_now_add=False)

    def clean(self):
        # Validación para asegurar que la calificación esté entre 1.0 y 5.0
        if self.rating < 1.0 or self.rating > 5.0:
            raise ValidationError('La calificación debe estar entre 1.0 y 5.0.')
        super().clean()  # Llamar a la validación de Django

    objects = ReseniaManager()

    def __str__(self):
        return self.book.title + ' - '+ str(self.rating)