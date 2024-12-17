# users/forms.py
from django import forms
from .models import CustomUser

class UserRegistrationForm(forms.ModelForm):
    # Campo de senha usando o widget PasswordInput
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['nome_completo', 'email', 'senha', 'especialidades', 'experiencia', 'agenda', 'tipo_usuario']

    def save(self, commit=True):
        # Criação do usuário sem salvar ainda
        user = super().save(commit=False)
        
        # Criptografando a senha antes de salvar
        user.set_password(self.cleaned_data['senha'])
        
        # Salva o usuário se commit for True
        if commit:
            user.save()
        return user