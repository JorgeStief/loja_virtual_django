from django.shortcuts import render
from django.http import HttpResponse
from catalogo.models import Categoria
from .forms import ContatoForm
from django.core.mail import send_mail
from django.conf import settings

def index(Request):
    return render(Request, 'index.html')


def contato(Request):
    categorias = Categoria.objects.all()
    success= False
    form = ContatoForm(Request.POST or None)
    if form.is_valid():
        form.send_mail()
        success= True
    context = {
        'form': form,
        'categorias': categorias,
        'success': success
    }
    return render(Request,'contato.html',context)


def produto(Request):
    return render(Request,'produto.html')


