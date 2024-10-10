
from django.urls import path
from debug_toolbar.toolbar import debug_toolbar_urls
from books.views import autores_view,editoriales_view, libros_view

urlpatterns = [
    path('autores/',autores_view),
    path('libros/',libros_view),
    path('editoriales/',editoriales_view),

] + debug_toolbar_urls()