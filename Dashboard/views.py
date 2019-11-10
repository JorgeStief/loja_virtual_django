from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator

from Dashboard.forms import ProdutoForm, RemoveProdutoForm
from catalogo.models import Produto, Categoria
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request, slug_da_categoria=None):
    categoria = None
    categorias = Categoria.objects.all()
    prod = Produto.objects.all()
    
    
    if slug_da_categoria:
        categoria = get_object_or_404(Categoria, slug=slug_da_categoria)
        prod = prod.filter(category=categoria).order_by("name")

    paginator = Paginator(prod, 5)
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


  

@login_required
def cadastra_produto(request):
    print("entrou1")
    if request.POST:
        print("entrou")
        produto_id = request.POST.get('id')
        if produto_id:
            produto = get_object_or_404(Produto, pk=produto_id)
            produto_form = ProdutoForm(request.POST, instance=produto)
        else:
            produto_form = ProdutoForm(request.POST)

        if produto_form.is_valid():
            produto = produto_form.save(commit=False)
            if produto_id:
                messages.add_message(request, messages.INFO, 'Produto alterado com sucesso!')
            else:
                produto.user = request.user
                messages.add_message(request, messages.INFO, 'Produto cadastrado com sucesso!')
            produto.save()
            return redirect('Dashboard:exibe_produto', id=produto.id)
        else:
            messages.add_message(request, messages.ERROR, 'Corrija o(s) erro(s) abaixo.')
    else:
        produto_form = ProdutoForm()

    

    return render(request, 'Dashboard/cadastra_produto.html', {
       'form': produto_form,
       
    })


def exibe_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form_remove_produto = RemoveProdutoForm(initial={'produto_id': id})
    return render(request, 'Dashboard/exibe_produto.html', {
       'produto': produto,
       'form_remove_produto': form_remove_produto
    })

def edita_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    produto_form = ProdutoForm(instance=produto)
    produto_form.fields['id'].initial = id

    
    return render(request, 'produto/cadastra_produto.html', {
       'form': produto_form,
       
    })

