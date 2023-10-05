from django.urls import path
from erp import views
from django.contrib.auth import views as auth_views
from . import views #adicionado para importar o site portal
from django.contrib.staticfiles.urls import staticfiles_urlpatterns#adicionado para importar o site portal

app_name = 'erp'

urlpatterns = [
    #  URL que corresponde à view do site portal
    path('', views.portal_index, name='portal_index'),

    #  URL que corresponde à view de registro
    path('registro/', views.registro, name='registro'),

    # GET /index
    path('', views.HomeView.as_view(), name="index"),
    
    #POST /Login
    path('../accounts/login/', auth_views.LoginView.as_view(), name='login'),
    
    #POST /Logout
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
        
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
    #path('categorias/', views.HomeCategoriasView.as_view(), name="index_categorias"),

    # GET /categorias/cadastrar
    #path('categorias/cadastrar', views.CriaCategoriasView.as_view(), name="cadastra_categorias"),

    # GET /categorias
    #path('categorias/lista', views.ListaCategoriasView.as_view(), name="lista_categorias"),

    # GET/POST /categorias/{pk}
    #path('categorias/<pk>', views.AtualizaCategoriasView.as_view(), name="atualiza_categorias"),

    # GET/POST /categorias/excluir/{pk}
    #path('categorias/excluir/<pk>', views.DeletaCategoriasView.as_view(), name="deleta_categorias"),
    
    #------------------
    # GET /estudante
    path('estudante/', views.HomeEstudanteView.as_view(), name="index_estudante"),

    # GET /estudante/cadastrar
    path('estudante/cadastrar', views.CriaEstudanteView.as_view(), name="cadastra_estudante"),

    # GET /estudante
    path('estudante/lista', views.ListaEstudanteView.as_view(), name="lista_estudante"),

    # GET/POST /estudante/{pk}
    path('estudante/<pk>', views.AtualizaEstudanteView.as_view(), name="atualiza_estudante"),

    # GET/POST /estudante/excluir/{pk}
    path('estudante/excluir/<pk>', views.DeletaEstudanteView.as_view(), name="deleta_estudante"),

]

urlpatterns += staticfiles_urlpatterns()