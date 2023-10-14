from django.shortcuts import render, redirect
from .forms import CadastroInstituicaoForm, CadastroEstudanteForm

def home(request):
    return render(request, 'index.html')

def cadastro_instituicao(request):
    if request.method == 'POST':
        form = CadastroInstituicaoForm(request.POST)
        if form.is_valid():
            # Lógica para salvar o cadastro da instituição no banco de dados
            form.save()
            return redirect('sucesso')  # Redireciona para a página de sucesso
    else:
        form = CadastroInstituicaoForm()
    return render(request, 'conta/cadastro_instituicao.html', {'form': form})

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
