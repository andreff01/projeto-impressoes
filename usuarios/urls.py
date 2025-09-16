from django.urls import path
from impressoes.views import painel_professor
from usuarios.views import CustomLoginView
from .views import registro_view

urlpatterns = [
    path('painel_professor/', painel_professor, name='painel_professor'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('registro/', registro_view, name='registro'),
]

