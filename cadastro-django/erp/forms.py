from core.models import Instituicao, Cursos, Estudante
from django import forms


# FORMULÁRIO DE INCLUSÃO DE INSTITUICÕES
# -------------------------------------------

class InsereInstituicaoForm(forms.ModelForm):

    class Meta:
        # Modelo base
        model = Instituicao

        # Campos que estarão no form
        fields = [
            #'cnpj',
            'nome',
            'cep',
            'endereco',
            'cidade',
            'uf',
            'telefone',
            'email',
            'site'
        ]


# FORMULÁRIO DE INCLUSÃO DE Cursos
# -------------------------------------------

class InsereCursosForm(forms.ModelForm):
    nome = forms.CharField(
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

    inscricao = forms.DateField(
        label='inscricao',
        required=True,
        widget=forms.SelectDateWidget()
    )
    
    class Meta:
        # Modelo base
        model = Cursos

        # Campos que estarão no form
        fields = [
            'nome',
            'descricao',
            'categoria',
            'inscricao'
        ]


# FORMULÁRIO DE INCLUSÃO DE Categorias
# -------------------------------------------

#class InsereCategoriasForm(forms.ModelForm):
#    nome = forms.CharField (
#        label = 'Nome',
#        required = True,
#        widget = forms.Textarea
#    )

#    descricao = forms.CharField(
#        label='Descrição',
#        required=True,
#        widget=forms.Textarea
#    )

#    class Meta:
        # Modelo base
#        model = Categorias

        # Campos que estarão no form
#        fields = [
#            'nome',
#            'descricao',
#        ]

#---------------------
# FORMULÁRIO DE INCLUSÃO DE ESTUDANTES
# -------------------------------------------

class InsereEstudanteForm(forms.ModelForm):
    
    data_nascimento = forms.DateField(
        label='nascimento',
        required=True,
        widget=forms.SelectDateWidget()
    )

    class Meta:
        # Modelo base
        model = Estudante

        # Campos que estarão no form
        fields = [
            'nome',
            'sobrenome',
            'data_nascimento',
            'telefone',
            'email',
            'sexo'
        ]


