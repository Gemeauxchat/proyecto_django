from django.shortcuts import render

#Vistas  generales de la aplicación

def libros_view(request):
    return render(request,'libros/libros.html')
