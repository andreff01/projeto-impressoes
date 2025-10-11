from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

class UsuarioCreationForm(UserCreationForm):
    tipo = forms.ChoiceField(choices=Usuario.TIPOS, label="Tipo de usuário")
    cpf = forms.CharField(label="CPF", max_length=14, required=True)
    endereco = forms.CharField(label="Endereço", max_length=255, required=True)
    telefone = forms.CharField(label="Telefone", max_length=20, required=True)

    class Meta:
        model = Usuario
        fields = ("username", "email", "password1", "password2", "tipo", "cpf", "endereco", "telefone")

    def save(self, commit=True):
        from django.contrib.auth.models import Group
        user = super().save(commit=False)
        user.tipo = self.cleaned_data["tipo"]
        user.cpf = self.cleaned_data["cpf"]
        user.endereco = self.cleaned_data["endereco"]
        user.telefone = self.cleaned_data["telefone"]
        if commit:
            user.save()
            # Adiciona o usuário ao grupo correto
            if user.tipo == "ADMIN":
                grupo = Group.objects.get(name="Administrador")
            else:
                grupo = Group.objects.get(name="Professor")
            user.groups.add(grupo)
        return user
