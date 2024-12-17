from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Rota principal para a página index
    path('login/', views.login_view, name='login'),  # Página de login
    path('cadastro/', views.cadastro_view, name='cadastro'),  # Página de cadastro
    path('test/', views.test_view, name='test'),  # Página test.html
    path('perfil/', views.perfil_view, name='perfil'),  # Página de perfil
    path('agenda/', views.agenda_view, name='agenda'),  # Página de agenda
    path('avaliacao/', views.avaliacao_view, name='avaliacao'),  # Página de avaliação
    path('cortes_agendados/', views.cortes_agendados_view, name='cortes_agendados'),  # Página de cortes agendados
    path('editar_perfil/', views.editar_perfil_view, name='editar_perfil'),  # Página de editar perfil
]