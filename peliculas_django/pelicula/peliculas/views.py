from django.shortcuts import render, redirect
from .models import Pelicula
from .forms import PeliculaForm

def agregar_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_peliculas')
    else:
        form = PeliculaForm()
    return render(request, 'peliculas/agregar.html', {'form': form})

def listar_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas/listar.html', {'peliculas': peliculas})
