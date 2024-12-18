"""reguahouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Mantém apenas uma vez
    path('meuapp/', include('meuapp.urls')),  # Rota para o app meuapp
    path('', include('meuapp.urls')),  # Rota para o app meuapp
    path('', include('users.urls')),  # Inclui as rotas da aplicação users
    path('usuarios/', include('users.urls')),  # Inclui as URLs de cadastro de usuário
]
