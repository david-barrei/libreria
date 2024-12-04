
from django.db import models
from django.db.models import Q, Count, Avg,Sum

class ReseniaManager(models.Manager):

    def promedio_resenia(self,libro_id):

        resultado = self.filter(
            book__id =libro_id
        ).aggregate(
            promedio_calificacion = Avg('rating'),
        )
        return resultado
    
    def resenia_libro(self,libro_id):

        resultado = self.filter(
            book__id =libro_id
        ).aggregate(
            promedio_resenias = Count('id'),
        )
        return resultado

def resenia_libro(self,libro_id):

        resultado = self.filter(
            book__id =libro_id
        ).aggregate(
            promedio_resenias = Count('id'),
        )
        return resultado



