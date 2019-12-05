from django.shortcuts import render
from django.http import HttpResponse
from catalogo.models import Categoria,Carrinho,Produto

from .forms import ContatoForm, CarrinhoForm, AtualizaProdutoCarrinhoForm
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from datetime import datetime, timedelta
from django.db.models import Sum, F, FloatField

class IndexView(TemplateView):

    template_name = 'produto_lista.html'


index = IndexView.as_view()

# @login_required
def contato(Request):
    
    success= False
    form = ContatoForm(Request.POST or None)
    if form.is_valid():
        form.send_mail()
        success= True
    context = {
        'form': form,
        'success': success
    }
    return render(Request,'contato.html',context)

@login_required
def minhaconta(Request):
    
    context = {
        "teste": "teste"
    }
    return render(Request,'minhaconta.html',context)

@login_required
def adiciona_produto_carrinho(request):
    if request.POST:
        user = request.user
        print(request.POST['pro_id'])
        if user:
            produto = Produto.objects.get(id=request.POST['pro_id'])
    
            carrinho = Carrinho()
            
            carrinho.user = request.user
            carrinho.produto = produto
            carrinho.quantidade = 1
            carrinho.preco = produto.price
            carrinho.save()

            
            resultado =  Carrinho.objects.filter(
                user=user,
            ).order_by('id')

            resultado = carrinho.aggregate(
            total=Sum(F('quantidade') * F('preco'), output_field=FloatField()))
   
            if resultado['total']:
                total = '{0:.2f}'.format(resultado['total'])
            else:
                total = '0,00'
            

            
            

            return render(request, 'carrinho.html', {
                'produtos': resultado,
                'total': total
            })

        else:
            raise ValueError('Ocorreu um erro inesperado ao tentar cadastrar um produto.')
    else:
        
        user = request.user
        carrinho = Carrinho.objects.filter(
            user=user,
        ).order_by('id')
        
        resultado = carrinho.aggregate(
        total=Sum(F('quantidade') * F('preco'), output_field=FloatField()))
        
        if resultado['total']:
            total = '{0:.2f}'.format(resultado['total'])
        else:
            total = '0,00'

        #sub-total_list = []
        lista_de_ids = []
        for car in carrinho:
            lista_de_ids.append(car.id)
            #lista_de_forms.append(AtualizaProdutoCarrinhoForm(initial={'quantidade': car.quantidade}))

        return render(request, 'carrinho.html', {
        
        'produtos': carrinho,
        'lista_de_ids':zip(lista_de_ids),
        'total': total
    })

def remove_produto_carrinho(request):
   carrinho_id = request.POST.get('prod_id')
   carrinho = get_object_or_404(Carrinho, id=carrinho_id)
   carrinho.delete()

   resultado = Produto.objects.all().aggregate(
       total=Sum(F('quantidade') * F('preco'), output_field=FloatField()))
   
   if resultado['total']:
      total = '{0:.2f}'.format(resultado['total'])
   else:
      total = '0,00'

   return render(request, 'produto/valor_do_estoque.html', {'total': total})

@login_required
class CarrinhoView(View):

    def post(self, request):
        return render(request,'carrinho.html',context)



    def get(self, request):
        print(request.user)
        context = {
        "teste": "teste"
        }
        return render(request,'carrinho.html',context)

