from django.db import models
from applications.libro.models import Libro
# Create your models here.

class Resenia(models.Model):
    book = models.ForeignKey(Libro, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    review_text = models.CharField(max_length=50)
    created_at = models.DateField( auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.book.title + ' - '+ str(self.rating)