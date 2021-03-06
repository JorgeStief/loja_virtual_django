from django.core.paginator import Paginator, InvalidPage
from .models import Produto, Categoria,Imagem, Carrinho
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from datetime import datetime, timedelta
from django.db.models import Sum, F, FloatField
from django.contrib.auth.decorators import login_required
ITEMS_PER_PAGE = 5

def produto_lista(request, slug_da_categoria=None):
    categoria = None
    categorias = Categoria.objects.all()
    prod = Produto.objects.all()
    
    
    if slug_da_categoria:
        categoria = get_object_or_404(Categoria, slug=slug_da_categoria)
        prod = prod.filter(category=categoria).order_by("name")

    paginator = Paginator(prod, ITEMS_PER_PAGE)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    context = {
        'categorias': categorias,
        'produtos': produtos,
        'categoria': categoria,
        
        }
    
    return render (request, 'catalogo/produto_lista.html',context)


def produto_exibe(request, slug_da_categoria, id ,slug_do_produto):
    
    produto = get_object_or_404(Produto, id=id)
    categoria = get_object_or_404(Categoria, id=produto.category_id)
    categorias = Categoria.objects.all().order_by('name')
    imagens =  Imagem.objects.filter(product=produto).order_by('id')
    
  
        
        
      

    context = {
        'produto': produto,
        'categorias': categorias,
        'categoria': categoria,
        'imagens': imagens,
    }
    return render(request, 'catalogo/produto_exibe.html', context)







