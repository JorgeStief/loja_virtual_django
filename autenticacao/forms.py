from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import PasswordInput
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.contrib.auth.models import User

class AuthenticationFormCustomizado(AuthenticationForm):

   error_messages = {
      'invalid_login': 'Login inválido',
   }

   username = forms.CharField(
      error_messages={'required': 'Campo obrigatório.', },
      widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '25'}),
      required=True)
   
   # <input type='text'
   #        name='username'
   #        id='id_username'
   #        class='form-control form-control-sm'
   #        maxlength='25'
   #        required>

   password = forms.CharField(
      error_messages={'required': 'Campo obrigatório.', },
      widget=PasswordInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '25'}),
      required=True)
   
   # <input type='password'
   #        name='password'
   #        id='id_password'
   #        class='form-control form-control-sm'
   #        maxlength='25'
   #        required>



  
    