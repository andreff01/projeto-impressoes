from django.db import models

class Impressora(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100, blank=True)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} ({self.localizacao})"
