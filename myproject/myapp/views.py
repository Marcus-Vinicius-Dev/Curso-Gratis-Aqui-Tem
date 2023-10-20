from django.shortcuts import render, redirect
from .forms import CadastroInstituicaoForm, CadastroEstudanteForm
from .models import Instituicao
from .forms import InstituicaoForm

def home(request):
    return render(request, 'index.html')

def cadastro_estudante(request):
    if request.method == 'POST':
        form = CadastroEstudanteForm(request.POST)
        if form.is_valid():
            # Lógica para salvar o cadastro do estudante no banco de dados
            form.save()
            return redirect('sucesso')  # Redireciona para a página de sucesso
    else:
        form = CadastroEstudanteForm()
    return render(request, 'conta/cadastro_estudante.html', {'form': form})

def escolher_tipo_conta(request):
    return render(request, 'conta/escolher_tipo_conta.html')

def sucesso(request):
    return render(request, 'conta/sucesso.html')

def cadastro_cursos_view(request):
    return render(request, 'conta/cadastro_cursos.html')

def cadastro_instituicao(request):
    if request.method == 'POST':
        form = CadastroInstituicaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_instituicoes')  
    else:
        form = CadastroInstituicaoForm()
    return render(request, 'conta/cadastro_instituicao.html', {'form': form})

def listar_instituicoes(request):
    instituicoes = Instituicao.objects.all()
    return render(request, 'conta/listar_instituicoes.html', {'instituicoes': instituicoes})

def cadastro_instituicao_form(request):
    if request.method == 'POST':
        form = CadastroInstituicaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_instituicoes')
    else:
        form = CadastroInstituicaoForm()
    return render(request, 'conta/cadastro_instituicao.html', {'form': form})

def cadastrar_instituicao(request):
    if request.method == 'POST':
        form = CadastroInstituicaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_instituicoes')  # Redireciona para a página de listagem de instituições
    else:
        form = CadastroInstituicaoForm()
    return render(request, 'conta/cadastro_instituicao.html', {'form': form})
