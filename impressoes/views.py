from django.shortcuts import render, redirect
from .models import PedidoDeImpressao
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test


@login_required
def criar_pedido(request):
    if request.method == 'POST':
        arquivo = request.FILES.get('arquivo')
        observacao = request.POST.get('observacao', '')
        if not arquivo:
            messages.error(request, 'Selecione um arquivo para impressão!')
        else:
            PedidoDeImpressao.objects.create(
                usuario=request.user,
                arquivo=arquivo,
                observacao=observacao
            )
            messages.success(request, 'Pedido de impressão enviado com sucesso!')
            return redirect('painel_professor')
    return render(request, 'impressoes/criar_pedido.html')


def is_admin(user):
    return user.is_authenticated and (hasattr(user, 'tipo') and user.tipo == 'admin')


@user_passes_test(is_admin)
def painel_admin(request):
    pedidos = PedidoDeImpressao.objects.all().order_by('-data_criacao')
    if request.method == 'POST':
        acao = request.POST.get('acao')
        pedido_id = request.POST.get('pedido_id')
        pedido = PedidoDeImpressao.objects.get(id=pedido_id)
        if acao == 'aprovar':
            pedido.status = 'aprovado'
            pedido.save()
            messages.success(request, 'Pedido aprovado!')
        elif acao == 'rejeitar':
            pedido.status = 'rejeitado'
            pedido.save()
            messages.success(request, 'Pedido rejeitado!')
        elif acao == 'excluir':
            pedido.delete()
            messages.success(request, 'Pedido excluído!')
        return redirect('painel_admin')
    return render(request, 'impressoes/painel_admin.html', {'pedidos': pedidos})


@login_required
def painel_professor(request):
    pedidos = PedidoDeImpressao.objects.filter(usuario=request.user).order_by('-data_criacao')
    if request.method == 'POST':
        acao = request.POST.get('acao')
        pedido_id = request.POST.get('pedido_id')
        pedido = PedidoDeImpressao.objects.get(id=pedido_id, usuario=request.user)
        if acao == 'excluir':
            pedido.delete()
            messages.success(request, 'Pedido excluído!')
        return redirect('painel_professor')
    return render(request, 'impressoes/painel_professor.html', {'pedidos': pedidos})


