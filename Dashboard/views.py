from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator

from Dashboard.forms import ProdutoForm, RemoveProdutoForm, PesquisaProdutoForm
from catalogo.models import Produto, Categoria
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    
    if request.user.is_superuser:   
        return render (request, 'Dashboard/home.html')
    else:

        return redirect ('/')  


  

@login_required
def cadastra_produto(request):
    if request.POST:
        produto_id = request.POST.get('id')
        
        if produto_id:
            produto = get_object_or_404(Produto, pk=produto_id)
            produto_form = ProdutoForm(request.POST, instance=produto)
            print(request.POST.get('main_image'))
            
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
            return redirect('Dashboard:lista_produto')
        else:
            messages.add_message(request, messages.ERROR, 'Corrija o(s) erro(s) abaixo.')
    else:
        produto_form = ProdutoForm()

    

    return render(request, 'Dashboard/cadastra_produto.html', {
       'form': produto_form,
       
    })


def exibe_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form_remove_produto = RemoveProdutoForm(initial={'id': id})
    return render(request, 'Dashboard/exibe_produto.html', {
       'produto': produto,
       'form_remove_produto': form_remove_produto
    })

def edita_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    produto_form = ProdutoForm(instance=produto)
    produto_form.fields['id'].initial = id

    
    return render(request, 'Dashboard/cadastra_produto.html', {
       'form': produto_form,
       
    })

def lista_produto(request):
    form = PesquisaProdutoForm(request.GET)
    
    if request.POST:  
        produto_id = request.POST.get('id')
        produto = get_object_or_404(Produto, id=produto_id)
        
        produto.delete()
        messages.add_message(request, messages.INFO, 'Produto removido com sucesso.')
        
    if form:
        if form.is_valid():
            busca_por = form.cleaned_data['busca_por']
            lista_de_produtos = Produto.objects.filter(name__icontains=busca_por).order_by('name')
    else:    
        lista_de_produtos = Produto.objects.all()

    paginator = Paginator(lista_de_produtos, 5)
    pagina = request.GET.get('page')
    produtos = paginator.get_page(pagina)
    
    return render(request, 'Dashboard/lista_produto.html', {
        'produtos': produtos,
        'form': form,
        'busca': busca_por
        
    })

def remove_produto(request):
#   form_remove_produto = RemoveProdutoForm(request.POST)
#   if form_remove_produto.is_valid:
      # produto_id = form_remove_produto.cleaned_data['produto_id']
    if request.POST:  
        produto_id = request.POST.get('id')
        produto = get_object_or_404(Produto, id=produto_id)
        
        produto.delete()
        messages.add_message(request, messages.INFO, 'Produto removido com sucesso.')
        produtos = Produto.objects.all()

    return render(request, 'Dashboard/lista_produto.html', {
        'produtos': produtos,
        
    })
#   else:
#      raise ValueError('Ocorreu um erro inesperado ao tentar remover um produto.')


      
