from decimal import Decimal
from django import forms
from django.core.validators import RegexValidator
from catalogo.models import Produto, Categoria
from projeto import settings
from datetime import datetime, timedelta


class PesquisaProdutoForm(forms.Form):
   class Meta:
      fields = ('busca_por')

   busca_por = forms.CharField(
      widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
      required=False)
   
   # <input type='text'
   #        name='busca_por'
   #        id='id_busca_por'
   #        class='form-control form-control-sm'
   #        maxlength='120'>

class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ('id', 'category', 'name', 'price', 'description','main_image')

    id = forms.CharField(widget=forms.HiddenInput(), required=False)

    # <input type="hidden" name="produto_id" id="id_produto_id" value="xxx">


    category = forms.ModelChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        queryset=Categoria.objects.all().order_by('name'),
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

    name = forms.CharField(
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

    price = forms.CharField(
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

    description = forms.CharField(
       widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
       required=False)
    
    # <input type='text'
    #        name='data_cadastro'
    #        class='form-control form-control-sm'
    #        required=''
    #        id='id_data_cadastro'
    #        maxlength='10'>


    main_image = forms.ImageField  (
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.ClearableFileInput(),
        required=False
    )
    

    def clean_price(self):
        price = self.cleaned_data.get('price')
        
        if not price:
            return price
        
        price = Decimal(price.replace(',', '.'))

        return price
        
    
        

class RemoveProdutoForm(forms.Form):
    class Meta:
        model = Produto
        fields = ('id')

    id = forms.CharField(widget=forms.HiddenInput(), required=True)

    # <input type="hidden" name="produto_id" id="id_produto_id" value="xxx">






















