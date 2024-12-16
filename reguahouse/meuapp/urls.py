from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('perfil/', views.perfil_view, name='perfil'),  # Página do perfil
    path('avaliacao/', views.avaliacao_view, name='avaliacao'),  # Página de avaliação
    path('cadastro/', views.cadastro, name='cadastro'),
    path('agenda/', views.agendar_corte, name='agendar_corte'),
    path('logout/', views.logout, name='logout'),

    

]