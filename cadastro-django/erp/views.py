from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from core.models import Instituicao, Cursos, Estudante
from erp.forms import InsereInstituicaoForm, InsereCursosForm, InsereEstudanteForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

################## Renderiza a página de registro ##########################

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SeuFormularioDeRegistro  # Importe o formulário de registro adequado

def registro(request):
    if request.method == 'POST':
        form = SeuFormularioDeRegistro(request.POST)
        if form.is_valid():
            user = form.save()
            # Faça login automaticamente após o registro
            login(request, user)
            return redirect('erp:index')  # Redirecione para a página inicial após o registro
    else:
        form = SeuFormularioDeRegistro()
    return render(request, 'registration.html', {'form': form})

################## Renderiza a página de registro ##########################

def index(request):
    return render(request, '../templates/index.html')

# PÁGINA PRINCIPAL
# ----------------------------------------------

class HomeView(TemplateView):
    template_name = "erp/index.html"


# PÁGINA PRINCIPAL INSTITUIÇÕES
# ----------------------------------------------

class HomeInstituicaoView(TemplateView):
    template_name = "erp/instituicao/index.html"


# LISTA DE INSTITUICOES
# ----------------------------------------------

class ListaInstituicaoView(ListView):
    template_name = "erp/instituicao/lista.html"
    model = Instituicao
    context_object_name = "instituicao"


# CADASTRAMENTO DE INSTITUICOES
# ----------------------------------------------

#@login_required
class CriaInstituicaoView(CreateView):
    template_name = "erp/instituicao/cria.html"
    model = Instituicao
    form_class = InsereInstituicaoForm
    success_url = reverse_lazy("erp:lista_instituicao")


# ATUALIZAÇÃO DE INSTITUICAO
# ----------------------------------------------

#@login_required
class AtualizaInstituicaoView(UpdateView):
    template_name = "erp/instituicao/atualiza.html"
    model = Instituicao
    fields = '__all__'
    context_object_name = 'instituicao'
    success_url = reverse_lazy("erp:lista_instituicao")


# EXCLUSÃO DE INSTITUICAO
# ----------------------------------------------

#@login_required
class DeletaInstituicaoView(DeleteView):
    template_name = "erp/instituicao/exclui.html"
    model = Instituicao
    context_object_name = 'instituicao'
    success_url = reverse_lazy("erp:lista_instituicao")


# PÁGINA PRINCIPAL CURSOS
# ----------------------------------------------

class HomeCursosView(TemplateView):
    template_name = "erp/cursos/index.html"


# LISTA DE CURSOS
# ----------------------------------------------

class ListaCursosView(ListView):
    template_name = "erp/cursos/lista.html"
    model = Cursos
    context_object_name = "cursos"


# CADASTRAMENTO DE CURSOS
# ----------------------------------------------

#@login_required
class CriaCursosView(CreateView):
    template_name = "erp/cursos/cria.html"
    model = Cursos
    form_class = InsereCursosForm
    success_url = reverse_lazy("erp:lista_cursos")


# ATUALIZAÇÃO DE CURSOS
# ----------------------------------------------

#@login_required
class AtualizaCursosView(UpdateView):
    template_name = "erp/cursos/atualiza.html"
    model = Cursos
    fields = '__all__'
    context_object_name = 'cursos'
    success_url = reverse_lazy("erp:lista_cursos")


# EXCLUSÃO DE CURSOS
# ----------------------------------------------

#@login_required
class DeletaCursosView(DeleteView):
    template_name = "erp/cursos/exclui.html"
    model = Cursos
    context_object_name = 'cursos'
    success_url = reverse_lazy("erp:lista_cursos")


# PÁGINA PRINCIPAL CATEGORIAS
# ----------------------------------------------

#class HomeCategoriasView(TemplateView):
#    template_name = "erp/categorias/index.html"


# LISTA DE CATEGORIAS
# ----------------------------------------------

#class ListaCategoriasView(ListView):
#    template_name = "erp/categorias/lista.html"
#    model = Categorias
#    context_object_name = "categorias"


# CADASTRAMENTO DE CATEGORIAS
# ----------------------------------------------

#@login_required
#class CriaCategoriasView(CreateView):
#    template_name = "erp/categorias/cria.html"
#    model = Categorias
#    form_class = InsereCategoriasForm
#    success_url = reverse_lazy("erp:lista_categorias")


# ATUALIZAÇÃO DE CATEGORIAS
# ----------------------------------------------

#@login_required
#class AtualizaCategoriasView(UpdateView):
#    template_name = "erp/categorias/atualiza.html"
#    model = Categorias
#    fields = '__all__'
#    context_object_name = 'categorias'
#    success_url = reverse_lazy("erp:lista_categorias")


# EXCLUSÃO DE CATEGORIAS
# ----------------------------------------------

#@login_required
#class DeletaCategoriasView(DeleteView):
#    template_name = "erp/categorias/exclui.html"
#    model = Categorias
#    context_object_name = 'categorias'
#    success_url = reverse_lazy("erp:lista_categorias")


# CADASTRAMENTO DE ESTUDANTES
# ----------------------------------------------

class HomeEstudanteView(TemplateView):
    template_name = "erp/estudante/index.html"
    
# LISTA DE ESTUDANTES
# ----------------------------------------------

class ListaEstudanteView(ListView):
    template_name = "erp/estudante/lista.html"
    model = Estudante
    context_object_name = "estudante"

#@login_required
class CriaEstudanteView(CreateView):
    template_name = "erp/estudante/cria.html"
    model = Estudante
    form_class = InsereEstudanteForm
    success_url = reverse_lazy("erp:lista_estudante")


# ATUALIZAÇÃO DE ESTUDANTES
# ----------------------------------------------

#@login_required
class AtualizaEstudanteView(UpdateView):
    template_name = "erp/estudante/atualiza.html"
    model = Estudante
    fields = '__all__'
    context_object_name = 'estudante'
    success_url = reverse_lazy("erp:lista_estudante")


# EXCLUSÃO DE ESTUDANTES
# ----------------------------------------------

#@login_required
class DeletaEstudanteView(DeleteView):
    template_name = "erp/estudante/exclui.html"
    model = Estudante
    context_object_name = 'estudante'
    success_url = reverse_lazy("erp:lista_estudante")

