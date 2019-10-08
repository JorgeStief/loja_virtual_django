from django.shortcuts import render
from django.http import HttpResponse
from catalogo.models import Categoria
from .forms import ContatoForm


def index(Request):
    return render(Request, 'index.html')


def contato(Request):

    categorias = Categoria.objects.all()
    form = ContatoForm()
    context = {
        'form': form,
        'categorias': categorias
    }
    return render(Request,'contato.html',context)


def produto(Request):
    return render(Request,'produto.html')


