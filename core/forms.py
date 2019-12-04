#
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from django.core.validators import RegexValidator
from catalogo.models import Carrinho, Categoria
from projeto import settings
from datetime import datetime, timedelta
class ContatoForm(forms.Form):


    name = forms.CharField(label='Nome',required=True)
    email = forms.EmailField(label='E-mail',required=True)
    message = forms.CharField(label='Mensagem',widget=forms.Textarea())

    #def __init__(self, *args, **kwargs):
        #super(ContatoForm,self).__init__(*args, **kwargs)
        #self.fields['name'].widget.attrs['class'] = 'form-control'
        #self.fields['email'].widget.attrs['class'] = 'form-control'
        #self.fields['message'].widget.attrs['class'] = 'form-control'


    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']

        message = 'Nome: {0}\n E-mail: {1}\n{2}'.format(name,email,message)
        send_mail(
            'Contato Loja Virtual Django', message, settings.DEFAULT_FROM_EMAIL, 
            [settings.DEFAULT_FROM_EMAIL]
        )
            
class AtualizaProdutoCarrinhoForm(forms.ModelForm):

    class Meta:
        model = Carrinho
        fields = ('quantidade',)

    quantidade = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        validators=[RegexValidator(regex='^[0-9]{1,5}$', message="Informe o valor no formato 99999.")],
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm quantidade',
                                      'maxlength': '5',
                                      'onkeypress': 'return event.charCode >= 48 && event.charCode <= 57'}),
        required=True)

class CarrinhoForm(forms.ModelForm):

    class Meta:
        model = Carrinho
        fields = ('produto_id','categoria', 'nome', 'quantidade', 'preco')

    produto_id = forms.CharField(widget=forms.HiddenInput(), required=False)

    # <input type="hidden" name="produto_id" id="id_produto_id" value="xxx">


    categoria = forms.ModelChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        queryset=Categoria.objects.all().order_by('nome'),
        empty_label='--- Selecione uma categoria ---',
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=True)

    #      {{ form.categoria }}
    #      <select name="categoria" class="form-control form-control-sm" required id="id_categoria">
    #          <option value="" selected>--- Selecione um(a) categoria ---</option>
    #          <option value="1">Categoria 1</option>
    #          <option value="2">Categoria 2</option>
    #          <option value="3">Categoria 3</option>
    #      </select>

    nome = forms.CharField(
        error_messages={'required': 'Campo obrigatório.',
                        'unique': 'Produto duplicado.'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
        required=True)

    # <input type="text"
    #        name="nome"
    #        id="id_nome"
    #        class="form-control form-control-sm"
    #        maxlength="120"
    #        required>

    quantidade = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        validators=[RegexValidator(regex='^[0-9]{1,5}$', message="Informe o valor no formato 99999.")],
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                      'maxlength': '5',
                                      'onkeypress': 'return event.charCode >= 48 && event.charCode <= 57'}),
        required=True)
    
    # NumberInput NÃO É SUPORTADO POR TODOS OS BROWSERS - EVITAR POR ENQUANTO

    # <input type='text'
    #        name='data_cadastro'
    #        class='form-control form-control-sm'
    #        required=''
    #        id='id_data_cadastro'
    #        maxlength='10'>

    preco = forms.CharField(
        localize=True,
        error_messages={'required': 'Campo obrigatório.', },
        validators=[RegexValidator(regex='^[0-9]{1,7}(,[0-9]{2})?$', message="Informe o valor no formato 9999999,99.")],
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                      'maxlength': '10',
                                      'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'}),
        required=True)

    # <input type="text"
    #        name="preco"
    #        id="id_preco"
    #        class="form-control form-control-sm"
    #        maxlength="10"
    #        onkeypress="return (event.charCode >= 48 &amp;&amp; event.charCode <= 57) || event.charCode == 44"
    #        required="">

    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        
        if not preco:
            return preco
        
        preco = Decimal(preco.replace(',', '.'))

        return preco
        
class RemoveProdutoCarrinhoForm(forms.Form):
    class Meta:
        fields = ('produto_id')

    produto_id = forms.CharField(widget=forms.HiddenInput(), required=True)

    # <input type="hidden" name="produto_id" id="id_produto_id" value="xxx">
       
