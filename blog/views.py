from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect
from .models import Articulo, Comentario
from .forms import ArticuloForm, ComentarioForm
from . import views


# Vista para mostrar todos los artículos
def lista_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'blog/lista_articulos.html', {'articulos': articulos})

# Vista para crear un nuevo artículo
def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_articulos')
    else:
        form = ArticuloForm()
    return render(request, 'blog/crear_articulo.html', {'form': form})

# Vista para agregar un comentario a un artículo
def agregar_comentario(request, articulo_id):
    articulo = Articulo.objects.get(id=articulo_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.articulo = articulo
            comentario.save()
            return redirect('lista_articulos')
    else:
        form = ComentarioForm()
    return render(request, 'blog/agregar_comentario.html', {'form': form, 'articulo': articulo})

# Revisar detalle del articulo
def detalle_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    comentarios = articulo.comentarios.all()  # Obtener todos los comentarios del artículo
    return render(request, 'blog/detalle_articulo.html', {'articulo': articulo, 'comentarios': comentarios})