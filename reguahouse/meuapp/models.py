from django.db import models



class Agendamento(models.Model):
    endereco = models.TextField()
    data = models.DateField()
    horario = models.TimeField()
    barbeiro = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.barbeiro} - {self.data} às {self.horario}"

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Barbeiro(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=200)
    especialidades = models.TextField()
    experiencia = models.CharField(max_length=200)
    agenda = models.CharField(max_length=200)

    def __str__(self):
        return self.nome