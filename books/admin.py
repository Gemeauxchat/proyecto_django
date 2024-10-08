from django.contrib import admin

from books.models import Autor, Editorial, Libro

# Register
# your models here..

class BookInline(admin.StackedInline):
    model = Libro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido","fecha_nacimiento","email", "telefono"]
    ordering=["-nombre"]
    

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display= ["nombre","ciudad","telefono","email","sitio_web","fecha_fundacion"]
    list_filter=["fecha_fundacion"]
    inlines = [
        BookInline,
    ]
    

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display=["titulo","isbn","idioma","fecha_publicacion","numero_paginas", "editorial"]
    
    search_fields=["titulo","autores__nombre"]
    filter_horizontal=["autores", ]