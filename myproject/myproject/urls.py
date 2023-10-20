from django.contrib import admin
from django.urls import path
from myapp import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cadastro/instituicao/', views.cadastro_instituicao_form, name='cadastro_instituicao'),
    path('cadastro/estudante/', views.cadastro_estudante, name='cadastro_estudante'),
    path('escolher_tipo_conta/', views.escolher_tipo_conta, name='escolher_tipo_conta'),
    path('sucesso/', views.sucesso, name='sucesso'),
    path('cadastro/cursos/', views.cadastro_cursos_view, name='cadastro_cursos'),
    path('listar/instituicoes/', views.listar_instituicoes, name='listar_instituicoes'),
]
