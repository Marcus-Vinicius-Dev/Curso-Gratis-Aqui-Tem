from django.urls.conf import include
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

#from . import views

urlpatterns = [
    path('', include('erp.urls', namespace='erp')),
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view (template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
