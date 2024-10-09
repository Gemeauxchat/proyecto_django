from django.contrib import admin
from books.models import Autor, Editorial, Libro
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register
# your models here..


class AutorResource(resources.ModelResource):
    class Meta:
        model =Autor
        fields = ('nombre','apellido','fecha_nacimiento')
        export_order = ('nombre','apellido','fecha_nacimiento')

class LibroInline(admin.StackedInline):
    model = Libro

@admin.register(Autor)
class AutorAdmin(ImportExportModelAdmin):
    resource_class = AutorResource
    list_display = ["nombre", "apellido","fecha_nacimiento","email", "telefono"]
    ordering=["-nombre"]
    

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display= ["nombre","ciudad","telefono","email","sitio_web","fecha_fundacion"]
    list_filter=["fecha_fundacion"]
    inlines = [
        LibroInline,
    ]
    

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display=["titulo","isbn","idioma","fecha_publicacion","numero_paginas", "editorial"]
    
    search_fields=["titulo","autores__nombre"]
    filter_horizontal=["autores", ]

