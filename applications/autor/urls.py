from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
    path('genero_libros/', views.Libros_genero.as_view(), name="genero"),
    
]
