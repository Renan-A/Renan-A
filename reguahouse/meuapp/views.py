from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Cliente, Barbeiro
from .models import Agendamento
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import BarbeiroForm  # Formulário específico para barbeiro (caso seja necessário)
from django.contrib.auth import get_user_model

User = get_user_model()  # Retorna o modelo de usuário configurado no projeto

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            user = User.objects.get(email=email)  # Busca o usuário pelo e-mail
        except User.DoesNotExist:
            user = None

        if user is not None and user.check_password(senha):  # Verifica a senha
            login(request, user)  # Realiza o login
            return redirect('test')  # Redireciona para a página 'test'
        else:
            messages.error(request, 'E-mail ou senha incorretos.')

    return render(request, 'login.html')

def test_view(request):
    return render(request, 'test.html')  # Renderiza a página de entrada

def logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def agendar_corte(request):
    if request.method == 'POST':
        endereco = request.POST.get('endereço')
        data = request.POST.get('data')
        horario = request.POST.get('horario')
        barbeiro = request.POST.get('barbeiro')

        # Salvar no banco de dados
        Agendamento.objects.create(
            endereco=endereco,
            data=data,
            horario=horario,
            barbeiro=barbeiro
        )

        return render(request, 'agenda.html', {'mensagem_sucesso': 'Agendamento realizado com sucesso!'})

    return render(request, 'agenda.html')


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        especialidades = request.POST.get('especialidades')
        experiencia = request.POST.get('experiencia')
        agenda = request.POST.get('agenda')

        if especialidades or experiencia or agenda:
            # Salvar barbeiro
            Barbeiro.objects.create(
                nome=nome,
                email=email,
                senha=senha,
                especialidades=especialidades,
                experiencia=experiencia,
                agenda=agenda
            )
        else:
            # Salvar cliente
            Cliente.objects.create(
                nome=nome,
                email=email,
                senha=senha
            )

        return redirect('perfil')  # Substitua pelo nome da URL de destino

    return render(request, 'cadastro')




def index(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def cadastro_view(request):
    return render(request, 'cadastro.html')

def test_view(request):
    return render(request, 'test.html')

def perfil_view(request):
    return render(request, 'perfil.html')

def agenda_view(request):
    return render(request, 'agenda.html')

def avaliacao_view(request):
    return render(request, 'avaliacao.html')

def cortes_agendados_view(request):
    return render(request, 'cortes-agendados.html')

def editar_perfil_view(request):
    return render(request, 'editar-perfil.html')

