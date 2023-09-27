from django.urls import path
from erp import views
from django.contrib.auth import views as auth_views
from . import views

app_name = 'erp'

urlpatterns = [
    #POST /Login
    path('../accounts/login/', auth_views.LoginView.as_view(), name='login'),
    
    #POST /Logout
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
        
    # GET /
    path('', views.HomeView.as_view(), name="index"),

    # GET /instituicao
    path('instituicao/', views.HomeInstituicaoView.as_view(), name="index_instituicao"),

    # GET /instituicao/cadastrar
    path('instituicao/cadastrar', views.CriaInstituicaoView.as_view(), name="cadastra_instituicao"),

    # GET /instituicao
    path('instituicao/lista', views.ListaInstituicaoView.as_view(), name="lista_instituicao"),

    # GET/POST /instituicao/{pk}
    path('instituicao/<pk>', views.AtualizaInstituicaoView.as_view(), name="atualiza_instituicao"),

    # GET/POST /instituicao/excluir/{pk}
    path('instituicao/excluir/<pk>', views.DeletaInstituicaoView.as_view(), name="deleta_instituicao"),

    # GET /cursos
    path('cursos/', views.HomeCursosView.as_view(), name="index_cursos"),

    # GET /cursos/cadastrar
    path('cursos/cadastrar', views.CriaCursosView.as_view(), name="cadastra_cursos"),

    # GET /cursos
    path('cursos/lista', views.ListaCursosView.as_view(), name="lista_cursos"),

    # GET/POST /cursos/{pk}
    path('cursos/<pk>', views.AtualizaCursosView.as_view(), name="atualiza_cursos"),

    # GET/POST /cursos/excluir/{pk}
    path('cursos/excluir/<pk>', views.DeletaCursosView.as_view(), name="deleta_cursos"),
    
    #---------------
    # GET /categorias
    path('categorias/', views.HomeCategoriasView.as_view(), name="index_categorias"),

    # GET /cursos/cadastrar
    path('categorias/cadastrar', views.CriaCategoriasView.as_view(), name="cadastra_categorias"),

    # GET /cursos
    path('categorias/lista', views.ListaCategoriasView.as_view(), name="lista_categorias"),

    # GET/POST /cursos/{pk}
    path('categorias/<pk>', views.AtualizaCategoriasView.as_view(), name="atualiza_categorias"),

    # GET/POST /cursos/excluir/{pk}
    path('categorias/excluir/<pk>', views.DeletaCategoriasView.as_view(), name="deleta_categorias"),
    
]
