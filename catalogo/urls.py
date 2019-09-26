from django.urls import path, re_path
from . import views

app_name='catalogo'

urlpatterns = [
    path("", views.produto_lista, name="produto_lista"),
    re_path(r'^(?P<slug>[\w_-]+)/$', views.categoria, name="categoria"),
]
