from django.shortcuts import render

#Vistas  generales de la aplicación


def autores_view(request):
    return render(request,'autores/autores.html')

