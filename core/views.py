from django.shortcuts import render
from django.http import HttpResponse


def index(Request):
    return render(Request,'index.html')


def contato(Request):
   return render(Request,'contato.html')


def produto(Request):
    return render(Request,'produto.html')


