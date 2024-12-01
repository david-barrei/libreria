from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Resenia
from .models import Libro
# Create your views here.

class Promedio_resenia(DetailView):
    model = Libro
    context_object_name = 'libro'
    template_name = 'resenia/listar.html'

    def get_context_data(self,**kwargs):

        context =super().get_context_data(**kwargs)
        book_id = self.object.id
        promedio =  Resenia.objects.promedio_resenia(book_id)
        context['promedio_calificacion'] = promedio.get('promedio_calificacion', 0)
        return context