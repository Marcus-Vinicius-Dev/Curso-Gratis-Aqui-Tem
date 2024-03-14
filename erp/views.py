from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from core.models import Instituicao, Cursos, Estudante, Usuario
from erp.forms import InsereInstituicaoForm, InsereCursosForm, InsereEstudanteForm, CustomUserCreationForm, BuscaCursosForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from django.http import JsonResponse
from django.views.generic.edit import FormView

from django.contrib.auth import views as auth_views #acrescentado em 14-03-24 por causa do erro de logout

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

class ListaInstituicaoView(ListView, LoginRequiredMixin):
    template_name = "erp/instituicao/lista.html"
    model = Instituicao
    context_object_name = "instituicao"

    def get_queryset(self):
        # Retorna apenas as instituições vinculadas ao usuário logado
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)




# CADASTRAMENTO DE INSTITUICOES
# ----------------------------------------------

#@login_required
class CriaInstituicaoView(CreateView):
    template_name = "erp/instituicao/cria.html"
    model = Instituicao
    form_class = InsereInstituicaoForm
    success_url = reverse_lazy("erp:lista_instituicao")

    def form_valid(self, form):
        form.instance.user = self.request.user  # Associe o usuário logado ao objeto
        return super().form_valid(form)


# ATUALIZAÇÃO DE INSTITUICAO
# ----------------------------------------------

#@login_required
class AtualizaInstituicaoView(UpdateView):
    template_name = "erp/instituicao/atualiza.html"
    model = Instituicao
    fields = '__all__'
    context_object_name = 'instituicao'
    success_url = reverse_lazy("erp:lista_instituicao")

    def form_valid(self, form):
        form.instance.user = self.request.user  # Associe o usuário logado ao objeto
        return super().form_valid(form)



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

class ListaCursosView(LoginRequiredMixin, ListView):
    template_name = "erp/cursos/lista.html"
    model = Cursos
    context_object_name = "cursos"

    def get_queryset(self):
        # Filtrar os cursos cuja instituição está vinculada ao usuário logado
        return Cursos.objetos.filter(instituicao__user=self.request.user)


# CADASTRAMENTO DE CURSOS
# ----------------------------------------------

#@login_required
class CriaCursosView(LoginRequiredMixin, CreateView):
    template_name = "erp/cursos/cria.html"
    model = Cursos
    form_class = InsereCursosForm

    def get_form_kwargs(self):
        # Passe o usuário logado como argumento para o formulário
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
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

def register_inst(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Faça login automaticamente após o registro
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'erp/register.html', {'form': form})



# def postagem(request):
#     # Receba o número de cursos a serem carregados (por exemplo, 5)
#     num_cursos = int(request.GET.get('num_cursos', 5))

#     # Consulta para buscar cursos adicionais
#     cursos = Cursos.objetos.all().order_by('-data_de_criacao')[:num_cursos]

#     # Serializa os cursos em JSON
#     cursos_data = []
#     for curso in cursos:
#         curso_data = {
#             'nome': curso.nome,
#             'descricao': curso.descricao,
#             'categoria': curso.categoria,
#             # Adicione outros campos, se necessário
#         }
#         cursos_data.append(curso_data)
    
#     context = {
#         'cursos': cursos,
#     }

#     # return JsonResponse({'cursos': cursos_data})
#     return render(request, 'erp/cursos/postagem.html', context)

# def load_more_cursos(request):
#     # Receba o número de cursos a serem carregados (por exemplo, 5)
#     num_cursos = int(request.GET.get('num_cursos', 5))

#     # Consulta para buscar cursos adicionais
#     cursos = Cursos.objetos.all().order_by('-data_de_criacao')[:num_cursos]

#     # Serializa os cursos em JSON
#     cursos_data = []
#     for curso in cursos:
#         curso_data = {
#             'nome': curso.nome,
#             'descricao': curso.descricao,
#             'categoria': curso.categoria,
#             # Adicione outros campos, se necessário
#         }
#         cursos_data.append(curso_data)

#     return JsonResponse({'cursos': cursos_data})

def postagem(request):
    # Consulta para buscar os três cursos mais recentes
    cursos_recentes = Cursos.objetos.all().order_by('-data_de_criacao')[:3]

    context = {
        'cursos_recentes': cursos_recentes,
    }

    return render(request, 'erp/cursos/postagem.html', context)


# funciona
def load_more_cursos(request):
    offset = int(request.GET.get('offset', 0))  # Offset inicial
    limit = 3  # Número de cursos a serem carregados de cada vez

    cursos = Cursos.objetos.order_by('-data_de_criacao')[offset:offset + limit]

    cursos_data = []
    for curso in cursos:
        curso_data = {
            'nome': curso.nome,
            'descricao': curso.descricao,
            'categoria': curso.categoria,
            'inscricao': curso.inscricao,
            'pk': curso.pk,
            'endereco': curso.instituicao.endereco ,
            'cidade': curso.instituicao.cidade ,
            'uf': curso.instituicao.uf ,
            'telefone': curso.instituicao.telefone ,
            'site': curso.instituicao.site ,
            # Adicione outros campos, se necessário
        }
        cursos_data.append(curso_data)

    return JsonResponse({'cursos': cursos_data})

def detalhes_curso(request, curso_id):
    curso = get_object_or_404(Cursos, pk=curso_id)
    # instituicao = curso.instituicao  # Acesse a instituição associada ao curso
    instituicao = get_object_or_404(Instituicao, nome=curso.instituicao)
    # instituicao = instituicao.objects.get(nome=curso.instituicao)
    return render(request, 'erp/cursos/detalhes.html', {'curso': curso})

# def load_more_cursos(request):
#     num_cursos = int(request.GET.get('num_cursos', 5))
#     cursos = Cursos.objetos.all().order_by('-data_de_criacao')[num_cursos:num_cursos+5]

#     cursos_data = []
#     for curso in cursos:
#         curso_data = {
#             'nome': curso.nome,
#             'descricao': curso.descricao,
#             'categoria': curso.categoria,
#             # Adicione outros campos, se necessário
#         }
#         cursos_data.append(curso_data)

#     return JsonResponse({'cursos': cursos_data})

def busca_cursos(request):
    cursos = Cursos.objetos.all()  # Obtenha todos os cursos inicialmente
    if request.method == 'POST':
        form = BuscaCursosForm(request.POST)
        if form.is_valid():
            categoria = form.cleaned_data.get('categoria')
            # Filtrar os cursos com base nos critérios de pesquisa
            if categoria:
                cursos = cursos.filter(categoria=categoria)
    else:
        form = BuscaCursosForm()

    context = {
        'form': form,
        'cursos': cursos,
    }
    return render(request, 'erp/cursos/busca_cursos.html', context)

class BuscaCursosView(FormView):
    template_name = "erp/cursos/busca_cursos.html"
    form_class = BuscaCursosForm  # Substitua por seu próprio formulário de pesquisa

    def form_valid(self, form):
        categoria = form.cleaned_data['categoria']  # Obtém a categoria escolhida pelo usuário
        cursos = Cursos.objetos.filter(categoria=categoria)  # Realiza a pesquisa no banco de dados
        context = {'form': form, 'cursos': cursos}
        return self.render_to_response(context)