from django.urls import path
from . import views

urlpatterns = [
    path('enviar/', views.enviar_impressao, name='enviar_impressao'),
    path('painel/', views.painel_admin, name='painel_admin'),
    path('meus-envios/', views.painel_professor, name='painel_professor'),
]
