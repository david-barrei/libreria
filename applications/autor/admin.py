from django.contrib import admin
from applications.autor.models import Autor, Genero
# Register your models here.

admin.site.register(Autor)
admin.site.register(Genero)
