from django.shortcuts import render

from .models import Produto, Categoria


def produto_lista(request):
    
    context = {
        'products': Produto.objects.all()
    }
    return render (request, 'catalogo/produto_lista.html',context)


def categoria(request,slug):
    category = Categoria.objects.get(slug=slug)
    context = {
        'current_category': category,
        'products': Produto.objects.filter(category=category),
    }
    return render (request, 'catalogo/categoria.html',context)
