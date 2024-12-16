from django import forms
from django.contrib.auth.models import User

class BarbeiroForm(forms.ModelForm):
    especialidades = forms.CharField(max_length=255)
    experiencia = forms.CharField(max_length=255)
    agenda = forms.CharField(max_length=255)

    class Meta:
        model = User  # Ou um modelo personalizado
        fields = ['especialidades', 'experiencia', 'agenda']