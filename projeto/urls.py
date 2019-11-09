"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from catalogo.models import Categoria

urlpatterns = [
    #path('',views.index, name='index'),
    path('admin/', include('Dashboard.urls',namespace='dashboard')),
    path('', include('core.urls',namespace='contato')),
    path('', include('core.urls',namespace='minhaconta')),
    path('', include('core.urls',namespace='carrinho')),
    #path('entrar/', LoginView.as_view(extra_context={'categorias': categorias}) ,name='login'),
    #path('sair/', LogoutView.as_view(next_page='/'),name='logout'),
    path('', include('catalogo.urls',namespace='catalogo')),
    path('autenticacao/', include('autenticacao.urls',namespace='autenticacao')),
    
]
