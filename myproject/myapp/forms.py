from django import forms
from .models import Instituicao

class CadastroInstituicaoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    cep = forms.CharField(label='CEP', max_length=10)
    endereco = forms.CharField(label='Endereço', max_length=100)
    cidade = forms.CharField(label='Cidade', max_length=100)
    uf = forms.CharField(label='UF', max_length=2)
    telefone = forms.CharField(label='Telefone', max_length=15)
    email = forms.EmailField(label='E-mail', max_length=100)
    site = forms.URLField(label='Site', max_length=100)

# forms.py

from django import forms
from .models import Instituicao

class InstituicaoForm(forms.ModelForm):
    class Meta:
        model = Instituicao
        fields = '__all__'

class CadastroEstudanteForm(forms.Form):
    # Defina os campos do formulário aqui
    nome = forms.CharField(max_length=100)
    # Outros campos...
