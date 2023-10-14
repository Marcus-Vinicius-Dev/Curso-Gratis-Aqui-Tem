from django.contrib import admin
from django.urls import path
from myapp.views import home, cadastro_instituicao, cadastro_estudante, sucesso

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cadastro/instituicao/', cadastro_instituicao, name='cadastro_instituicao'),
    path('cadastro/estudante/', cadastro_estudante, name='cadastro_estudante'),
    path('sucesso/', sucesso, name='sucesso'),
]
