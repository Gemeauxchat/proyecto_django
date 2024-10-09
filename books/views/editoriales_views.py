from django.shortcuts import render

#Vistas  generales de la aplicación

def editoriales_view(request):
    return render(request,'editoriales/editorial.html')

