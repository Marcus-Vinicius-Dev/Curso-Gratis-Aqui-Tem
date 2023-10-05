from django.shortcuts import render

# Create your views here.
def minha_pagina(request):
    return render(request, 'curso/minha_pagina.html')