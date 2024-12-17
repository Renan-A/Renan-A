# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nome_completo = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    # Campos adicionais
    especialidades = models.CharField(max_length=255, blank=True, null=True)
    experiencia = models.CharField(max_length=255, blank=True, null=True)
    agenda = models.CharField(max_length=255, blank=True, null=True)

    TIPOS_USUARIO = [
        ('cliente', 'Cliente'),
        ('barbeiro', 'Barbeiro'),
    ]
    tipo_usuario = models.CharField(max_length=8, choices=TIPOS_USUARIO, default='cliente')

    def __str__(self):
        return self.nome_completo
