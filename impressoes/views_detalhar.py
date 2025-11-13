from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import PedidoDeImpressao

@login_required
def detalhar_pedido(request, pedido_id):
    pedido = get_object_or_404(PedidoDeImpressao, id=pedido_id, usuario=request.user)
    return render(request, 'impressoes/detalhar_pedido.html', {'pedido': pedido})
