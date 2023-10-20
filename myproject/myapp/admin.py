from django.contrib import admin
from .models import Instituicao  

# Registre o modelo Instituicao para ser gerenciado pelo Django Admin
admin.site.register(Instituicao)
