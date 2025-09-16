from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

class UsuarioCreationForm(UserCreationForm):
    tipo = forms.ChoiceField(choices=Usuario.TIPOS, label="Tipo de usuário")

    class Meta:
        model = Usuario
        fields = ("username", "email", "password1", "password2", "tipo")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.tipo = self.cleaned_data["tipo"]
        if commit:
            user.save()
        return user
