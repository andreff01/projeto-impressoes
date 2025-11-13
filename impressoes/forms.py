
from django import forms

class PedidoDeImpressaoForm(forms.Form):
    arquivos = forms.FileField(
        required=True,
        label='Arquivo'
    )
    quantidade_documentos = forms.IntegerField(min_value=1, label='Quantidade de documentos')
    quantidade_folhas = forms.IntegerField(min_value=1, label='Quantidade de folhas')
    frente_verso = forms.BooleanField(required=False, label='Impressão frente e verso')
    grampear = forms.BooleanField(required=False, label='Grampear')
    tipo_impressao = forms.ChoiceField(
        choices=[('pb', 'Preto e Branco'), ('colorida', 'Colorida')],
        label='Tipo de impressão'
    )
    observacao = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False, label='Observação')
