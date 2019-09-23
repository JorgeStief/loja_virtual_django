from django.shortcuts import render
from django.http import HttpResponse
def index(Request):
    context = {
        'title': 'Ecommerce'
    }
    return render(Request,'index.html',context)


def contato(Request):
    
    return render(Request,'contato.html')


def produto(Request):
    
    return render(Request,'produto.html')

def lista_produtos(Request):
    
    return render(Request,'produtos_lista.html')
