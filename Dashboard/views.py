from django.shortcuts import render, redirect
from django.http import HttpResponse
from catalogo.models import Categoria, Produto
from django.conf import settings
from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage
from django.shortcuts import render, get_object_or_404
ITEMS_PER_PAGE = 5

# Create your views here.
@login_required
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
    if request.user.is_superuser:   
        return render (request, 'Dashboard/index.html',context)
    else:

        return redirect ('/')  
    
