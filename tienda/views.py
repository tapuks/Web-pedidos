from django.shortcuts import render

# Create your views here.
from tienda.models import CategoriaProd, Producto


def tienda(request):
    categoriasProd = CategoriaProd.objects.all()
    productos = Producto.objects.all()
    return render(request, 'tienda.html', {'categoriasProd': categoriasProd, 'productos': productos})