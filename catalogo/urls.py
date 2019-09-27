from django.urls import path
from . import views

app_name='catalogo'

urlpatterns = [
    path('', views.produto_lista, name="produto_lista"),
    path('<slug:slug_da_categoria>/', views.produto_lista, name="produto_lista_por_categoria"),
    #re_path(r'^(?P<slug>[\w_-]+)/$', views.categoria, name="categoria"),
    path('<int:id>/<slug:slug_do_produto>/', views.produto_exibe, name='produto_exibe'),
]
