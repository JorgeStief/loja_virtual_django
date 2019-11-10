from django.urls import path
from Dashboard import views

app_name='Dashboard'

urlpatterns = [
    path('', views.index, name="Dashboard"),
    path('cadastra_produto/', views.cadastra_produto, name='cadastra_produto'),
    path('exibe_produto/<int:id>/', views.exibe_produto, name='exibe_produto'),
    path('edita_produto/<int:id>/', views.edita_produto, name='edita_produto'),
    #path('remove_produto/', views.remove_produto, name='remove_produto'),
    #path('pesquisa_produto/', views.pesquisa_produto, name='pesquisa_produto'),
    #path('lista_produto/', views.lista_produto, name='lista_produto'),
    #path('<slug:slug_da_categoria>/', views.produto_lista, name="produto_lista_por_categoria"),
    #re_path(r'^(?P<slug>[\w_-]+)/$', views.categoria, name="categoria"),
    #path('<slug:slug_da_categoria>/<int:id>/<slug:slug_do_produto>/', views.produto_exibe, name='produto_exibe'),
]
