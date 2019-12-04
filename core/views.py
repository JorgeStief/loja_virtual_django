from django.shortcuts import render
from django.http import HttpResponse
from catalogo.models import Categoria,Carrinho

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
        carrinho_form = CarrinhoForm(request.POST)

        if carrinho_form.is_valid():
            carrinho = carrinho_form.save(commit=False)
            carrinho.user = request.user
            carrinho.save()

            resultado = Carrinho.objects.all().aggregate(
                total=Sum(F('quantidade') * F('preco'), output_field=FloatField()))
            if resultado['total']:
                total = '{0:.2f}'.format(resultado['total'])
            else:
                total = '0,00'

            lista = []
            lista.append(carrinho)
            lista_de_forms = []
            lista_de_forms.append(AtualizaProdutoCarrinhoForm(initial={'quantidade': carrinho.quantidade}))

            return render(request, 'carrinho.html', {
                'listas': zip(lista, lista_de_forms),
                'total': total
            })

        else:
            raise ValueError('Ocorreu um erro inesperado ao tentar cadastrar um produto.')
    else:
        carrinho_form = CarrinhoForm()
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

    lista_de_ids = []
    lista_de_forms = []
    for car in carrinho:
        lista_de_ids.append(car.id)
        lista_de_forms.append(AtualizaProdutoCarrinhoForm(initial={'quantidade': car.quantidade}))

    return render(request, 'carrinho.html', {
      'form': carrinho_form,
      'listas': zip(carrinho, lista_de_forms),
      'lista_de_ids': lista_de_ids,
      'total': total
   })



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

