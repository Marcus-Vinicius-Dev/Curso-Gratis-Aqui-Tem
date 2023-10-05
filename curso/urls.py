from django.urls import path
from . import views

urlpatterns = [
    path('minha-pagina/', views.minha_pagina, name='minha_pagina'),
]