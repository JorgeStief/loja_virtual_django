from django.urls import path
from . import views


app_name='core'

urlpatterns = [
    path('contato/', views.contato, name="contato"),
    path('minhaconta/', views.minhaconta, name="minhaconta"),
    path('carrinho/', views.adiciona_produto_carrinho, name='carrinho'),

    
]
