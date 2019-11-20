from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
# Create your views here.

User =  get_user_model

class  RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    model = User
    success_url = reverse_lazy('catalogo:produto_lista')


