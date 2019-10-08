#
from django import forms


class ContatoForm(forms.Form):


    name = forms.CharField(label='Nome',required=True)
    email = forms.EmailField(label='E-mail',required=True)
    message = forms.CharField(label='Mensagem',widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContatoForm,self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['class'] = 'form-control'
        
