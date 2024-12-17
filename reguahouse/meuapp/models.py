from django.db import models

# Gerenciador de Usuários Customizado
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O campo E-mail é obrigatório.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


# Modelo Customizado de Usuário
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)  # E-mail como identificador principal
    nome = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.email



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