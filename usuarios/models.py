from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    TIPOS = (
        ('professor', 'Professor'),
        ('admin', 'Administrador'),
    )
    tipo = models.CharField(max_length=20, choices=TIPOS)

    def __str__(self):
        return self.username
