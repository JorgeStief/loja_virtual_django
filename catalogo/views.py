from django.shortcuts import render, get_object_or_404

from .models import Produto, Categoria,Imagem


def produto_lista(request, slug_da_categoria=None):
    categoria = None
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all()
    
    if slug_da_categoria:
        categoria = get_object_or_404(Categoria, slug=slug_da_categoria)
        produtos = produtos.filter(category=categoria).order_by("name")
    context = {'categorias': categorias,
               'produtos': produtos,
               'categoria': categoria}
    
    return render (request, 'catalogo/produto_lista.html',context)


def produto_exibe(request, id ,slug_do_produto):
    
    produto = get_object_or_404(Produto, id=id)
    categoria = get_object_or_404(Categoria, id=produto.category_id)
    categorias = Categoria.objects.all().order_by('name')
    imagens =  Imagem.objects.all().filter(product=produto).order_by('id')
    # Esta view espera receber o id do produto e seu slug para recuperar o produto
    # Podemos recuperar o produto apenas com o seu id uma vez que ele é unique.
    # Incluímos o slug para podermos construir 'SEO friendly URLs'.
    # SEO = Search Engine Optimization.
    # Exemplo: http://www.dominio.com.br/produto?id=721 <== Ruim
    # Exemplo: http://www.dominio.com.br/721/notebook-del-vostro-3458-i3 <== Bom
    aux=[]
    i=0
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
