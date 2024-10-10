from django.shortcuts import render

# Create your views here.
def autores_view(request):
    return render(request,'autores/autores.html')

def editoriales_view(request):
    return render(request,'editoriales/editorial.html')

def libros_view(request):
    return render(request,'libros/libros.html')
