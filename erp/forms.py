from core.models import Instituicao, Cursos, Estudante, Usuario
from django import forms

from django.contrib.auth.forms import UserCreationForm


# FORMULÁRIO DE INCLUSÃO DE INSTITUICÕES
# -------------------------------------------

class InsereInstituicaoForm(forms.ModelForm):

    user = forms.ModelChoiceField(
        queryset=Usuario.objects.all(),
        widget=forms.HiddenInput,
        required=False
    )

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
            'site',
            'user'
        ]
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Obtenha o usuário do kwargs
        super(InsereInstituicaoForm, self).__init__(*args, **kwargs)

        # Se o usuário estiver logado, defina o valor do campo user como o usuário atual
        if user:
            self.fields['user'].initial = user


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

    # categoria = forms.CharField(
    #     label='Categoria',
    #     required=True,
    #     widget=forms.Textarea
    # )
    categoria = forms.ChoiceField(
        choices=Cursos.CATEGORIAS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    inscricao = forms.DateField(
        label='inscricao',
        required=True,
        widget=forms.SelectDateWidget()
    )

    instituicao = forms.ModelChoiceField(
        label='Instituição',
        required=True,
        queryset=Instituicao.objetos.none() ,  # Preencher com todas as instituições
        empty_label=None  # Para garantir que seja selecionada uma instituição
    )
    def __init__(self, user, *args, **kwargs):
        super(InsereCursosForm, self).__init__(*args, **kwargs)
        # Filtra as opções do campo de instituição com base no usuário logado
        self.fields['instituicao'].queryset = Instituicao.objetos.filter(user=user)
    
    class Meta:
        # Modelo base
        model = Cursos

        # Campos que estarão no form
        fields = [
            'nome',
            'descricao',
            'categoria',
            'inscricao',
            'instituicao'
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

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = UserCreationForm.Meta.fields + ('email',)

class BuscaCursosForm(forms.Form):
    categoria = forms.ChoiceField(
        choices=Cursos.CATEGORIAS_CHOICES,
        required=False,
    )