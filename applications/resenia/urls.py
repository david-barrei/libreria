
from django.urls import path

from .import views

urlpatterns = [
    path('reseña/<int:pk>/', views.Promedio_resenia.as_view(), name="detalle_libro"),
    
]









