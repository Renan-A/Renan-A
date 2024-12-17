# users/views.py
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o usuário no banco de dados
            return redirect('login')  # Redireciona para a página de login
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})
