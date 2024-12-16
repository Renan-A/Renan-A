from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Cliente, Barbeiro
from .models import Agendamento
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import BarbeiroForm  # Formulário específico para barbeiro (caso seja necessário)

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Autenticar o usuário (substituir com username se necessário)
        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirecione para a página principal ou dashboard
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')

    return render(request, 'login.html')

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

        return render(request, 'agendar.html', {'mensagem_sucesso': 'Agendamento realizado com sucesso!'})

    return render(request, 'agendar.html')


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

        return redirect('home')  # Substitua pelo nome da URL de destino

    return render(request, 'cadastro.html')




def home_view(request):
    return render(request, 'meuapp/home.html')

def avaliacao_view(request):
    return render(request, 'meuapp/avaliacao.html')

def perfil_view(request):
    return render(request, 'meuapp/perfil.html')

def agendar_corte(request):
    return render(request, 'agendamento/agendar_corte.html')





