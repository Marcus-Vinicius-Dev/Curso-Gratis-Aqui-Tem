from django import forms

class CadastroInstituicaoForm(forms.Form):
    # Defina os campos do formulário aqui
    nome = forms.CharField(max_length=100)
    # Outros campos...

class CadastroEstudanteForm(forms.Form):
    # Defina os campos do formulário aqui
    nome = forms.CharField(max_length=100)
    # Outros campos...
