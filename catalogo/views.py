from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, InvalidPage
from .models import Produto, Categoria,Imagem
ITEMS_PER_PAGE = 5

def produto_lista(request, slug_da_categoria=None):
    categoria = None
    categorias = Categoria.objects.all()
    prod = Produto.objects.all()
    
    if slug_da_categoria:
        categoria = get_object_or_404(Categoria, slug=slug_da_categoria)
        prod = prod.filter(category=categoria).order_by("name")

    paginator = Paginator(prod, 1)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    context = {
        'categorias': categorias,
        'produtos': produtos,
        'categoria': categoria,
        }
    
    return render (request, 'catalogo/produto_lista.html',context)


def produto_exibe(request, id ,slug_do_produto):
    
    produto = get_object_or_404(Produto, id=id)
    categoria = get_object_or_404(Categoria, id=produto.category_id)
    categorias = Categoria.objects.all().order_by('name')
    imagens =  Imagem.objects.all().filter(product=produto).order_by('id')
    
    aux=[]
    aux1 = ''
    i=0
    if imagens != '':
        for imagem in imagens:
            if i==0:
                aux1= imagem.slug
            else:
                aux.append(imagem.slug) 
            i = i+1    
        
        
      

    context = {
        'produto': produto,
        'categorias': categorias,
        'categoria': categoria,
        'imagens': aux,
        'imagem': aux1
    }
    return render(request, 'catalogo/produto_exibe.html', context)
