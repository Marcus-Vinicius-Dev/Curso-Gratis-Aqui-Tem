from core.models import Instituicao, Cursos, Categorias
from django import forms



# FORMULÁRIO DE INCLUSÃO DE INSTITUICÕES
# -------------------------------------------

class InsereInstituicaoForm(forms.ModelForm):

    class Meta:
        # Modelo base
        model = Instituicao

        # Campos que estarão no form
        fields = [
            'cnpj',
            'nome',
            'cep',
            'endereco',
            'uf',
            'telefone',
            'email'
        ]


# FORMULÁRIO DE INCLUSÃO DE Cursos
# -------------------------------------------

class InsereCursosForm(forms.ModelForm):
    nome = forms.CharField (
        label = 'Nome',
        required = True,
        widget = forms.Textarea
    )

    descricao = forms.CharField(
        label='Descrição',
        required=True,
        widget=forms.Textarea
    )

    categoria = forms.CharField(
        label='Categoria',
        required=True,
        widget=forms.Textarea
    )

    class Meta:
        # Modelo base
        model = Cursos

        # Campos que estarão no form
        fields = [
            'nome',
            'descricao',
            'categoria'
        ]


# FORMULÁRIO DE INCLUSÃO DE Categorias
# -------------------------------------------

class InsereCategoriasForm(forms.ModelForm):
    nome = forms.CharField (
        label = 'Nome',
        required = True,
        widget = forms.Textarea
    )

    descricao = forms.CharField(
        label='Descrição',
        required=True,
        widget=forms.Textarea
    )

    class Meta:
        # Modelo base
        model = Categorias

        # Campos que estarão no form
        fields = [
            'nome',
            'descricao',
        ]
