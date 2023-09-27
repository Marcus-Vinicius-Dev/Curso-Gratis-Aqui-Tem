from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from core.models import Instituicao, Cursos, Categorias
from erp.forms import InsereCategoriasForm, InsereInstituicaoForm, InsereCursosForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

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

class CriaInstituicaoView(CreateView):
    template_name = "erp/instituicao/cria.html"
    model = Instituicao
    form_class = InsereInstituicaoForm
    success_url = reverse_lazy("erp:lista_instituicao")


# ATUALIZAÇÃO DE INSTITUICAO
# ----------------------------------------------

class AtualizaInstituicaoView(UpdateView):
    template_name = "erp/instituicao/atualiza.html"
    model = Instituicao
    fields = '__all__'
    context_object_name = 'instituicao'
    success_url = reverse_lazy("erp:lista_instituicao")


# EXCLUSÃO DE INSTITUICAO
# ----------------------------------------------

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

class CriaCursosView(CreateView):
    template_name = "erp/cursos/cria.html"
    model = Cursos
    form_class = InsereCursosForm
    success_url = reverse_lazy("erp:lista_cursos")


# ATUALIZAÇÃO DE CURSOS
# ----------------------------------------------

class AtualizaCursosView(UpdateView):
    template_name = "erp/cursos/atualiza.html"
    model = Cursos
    fields = '__all__'
    context_object_name = 'cursos'
    success_url = reverse_lazy("erp:lista_cursos")


# EXCLUSÃO DE CURSOS
# ----------------------------------------------

class DeletaCursosView(DeleteView):
    template_name = "erp/cursos/exclui.html"
    model = Cursos
    context_object_name = 'cursos'
    success_url = reverse_lazy("erp:lista_cursos")


# PÁGINA PRINCIPAL CATEGORIAS
# ----------------------------------------------

class HomeCategoriasView(TemplateView):
    template_name = "erp/categorias/index.html"


# LISTA DE CATEGORIAS
# ----------------------------------------------

class ListaCategoriasView(ListView):
    template_name = "erp/categorias/lista.html"
    model = Categorias
    context_object_name = "categorias"


# CADASTRAMENTO DE CURSOS
# ----------------------------------------------

class CriaCategoriasView(CreateView):
    template_name = "erp/categorias/cria.html"
    model = Categorias
    form_class = InsereCategoriasForm
    success_url = reverse_lazy("erp:lista_categorias")


# ATUALIZAÇÃO DE CATEGORIAS
# ----------------------------------------------

class AtualizaCategoriasView(UpdateView):
    template_name = "erp/categorias/atualiza.html"
    model = Categorias
    fields = '__all__'
    context_object_name = 'categorias'
    success_url = reverse_lazy("erp:lista_categorias")


# EXCLUSÃO DE CURSOS
# ----------------------------------------------

class DeletaCategoriasView(DeleteView):
    template_name = "erp/categorias/exclui.html"
    model = Categorias
    context_object_name = 'categorias'
    success_url = reverse_lazy("erp:lista_categorias")
