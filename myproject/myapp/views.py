from django.shortcuts import render
from .forms import CadastroInstituicaoForm, CadastroEstudanteForm

def home(request):
    return render(request, 'index.html')

def cadastro_instituicao(request):
    if request.method == 'POST':
        form = CadastroInstituicaoForm(request.POST)
        if form.is_valid():
            # Lógica para salvar o cadastro da instituição
            return render(request, 'sucesso.html')  # Página de sucesso após o cadastro
    else:
        form = CadastroInstituicaoForm()
    return render(request, 'cadastro_instituicao.html', {'form': form})

def cadastro_estudante(request):
    if request.method == 'POST':
        form = CadastroEstudanteForm(request.POST)
        if form.is_valid():
            # Lógica para salvar o cadastro do estudante
            return render(request, 'sucesso.html')  # Página de sucesso após o cadastro
    else:
        form = CadastroEstudanteForm()
    return render(request, 'cadastro_estudante.html', {'form': form})
