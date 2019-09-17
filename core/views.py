from django.shortcuts import render
from django.http import HttpResponse
def index(Request):
    context = {
        'title': 'Ecommerce'
    }
    return render(Request,'index.html',context)
