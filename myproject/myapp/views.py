from django.shortcuts import render, redirect
from .forms import CadastroInstituicaoForm, CadastroEstudanteForm
from .models import Instituicao

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

def cadastro_cursos_view(request):
    return render(request, 'conta/cadastro_cursos.html')

def cadastrar_instituicao(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        cep = request.POST['cep']
        endereco = request.POST['endereco']
        cidade = request.POST['cidade']
        uf = request.POST['uf']
        telefone = request.POST['telefone']
        email = request.POST['email']
        site = request.POST['site']

        instituicao = Instituicao(
            nome=nome,
            cep=cep,
            endereco=endereco,
            cidade=cidade,
            uf=uf,
            telefone=telefone,
            email=email,
            site=site
        )
        instituicao.save()

        return redirect('cadastro_cursos')  # Redireciona para a próxima página após o cadastro

    return render(request, 'conta/cadastro_instituicao.html')