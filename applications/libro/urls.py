
from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('libros/', views.ListLibros.as_view(), name="listar_libros"),
    path('libro_filtrar/', views.Genero_libro.as_view(), name="genero"),
]






