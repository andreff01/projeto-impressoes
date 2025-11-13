from django import forms
from .models_impressora import Impressora

class ImpressoraForm(forms.ModelForm):
    class Meta:
        model = Impressora
        fields = ['nome', 'localizacao', 'modelo', 'ativa']
