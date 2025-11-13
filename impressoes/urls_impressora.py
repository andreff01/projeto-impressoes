from django.urls import path
from . import views_impressora

urlpatterns = [
    path('impressoras/', views_impressora.listar_impressoras, name='listar_impressoras'),
    path('impressoras/nova/', views_impressora.criar_impressora, name='criar_impressora'),
    path('impressoras/editar/<int:impressora_id>/', views_impressora.editar_impressora, name='editar_impressora'),
    path('impressoras/excluir/<int:impressora_id>/', views_impressora.excluir_impressora, name='excluir_impressora'),
]
