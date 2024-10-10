from django.shortcuts import render

# Create your views here.
def autores_view(request):
    autores = [ 
        {"id":1, "nombre": "Antonio"},
        {"id":2, "nombre": "Matilde"},
        {"id":3, "nombre": "Felipe"},
    ]
    context = {"autores": autores, "titulo":"Hola esto es una prueba"}
    return render(request,'autores/autores.html', context)

def autor_detail(request, id):
    autores = [
        {"id":1, "nombre":"Antonio"},
        {"id":2, "nombre":"Matilde"},
        {"id":3, "nombre":"Felipe"},
    ]
    context = {
        'autor':None
        }
    for autor in autores:
        
        if autor['id'] == id:
            context['autor'] = autor
    return render(request, 'autores/autor_detail.html', context)

def editoriales_view(request):
    return render(request,'editoriales/editorial.html')

def libros_view(request):
    return render(request,'libros/libros.html')
