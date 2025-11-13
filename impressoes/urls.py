from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_pedido, name='criar_pedido'),
    path('painel/', views.painel_admin, name='painel_admin'),
    path('meus-envios/', views.painel_professor, name='painel_professor'),
    path('pedido/<int:pedido_id>/', views.detalhar_pedido, name='detalhar_pedido'),
]
