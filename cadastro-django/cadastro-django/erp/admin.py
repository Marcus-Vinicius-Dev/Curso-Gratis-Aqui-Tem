from django.contrib import admin
from core.models import Estudante, Instituicao, Cursos
#from core.models import Instituicao

# Register your models here.
admin.site.register(Instituicao)
admin.site.register(Estudante)
admin.site.register(Cursos)
