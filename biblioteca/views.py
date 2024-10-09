from django.shortcuts import render

#Vistas  generales de la aplicación
def home_view(request):
    return render(request,'general/home.html')

def contact_view(request):
    return render(request,'general/contact.html')

def autores_view(request):
    return render(request,'autores/autores.html')

def editoriales_view(request):
    return render(request,'editoriales/editorial.html')

def libros_view(request):
    return render(request,'libros/libros.html')
