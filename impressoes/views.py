from django.shortcuts import render, redirect, get_object_or_404
from .models import PedidoDeImpressao, ArquivoPedido
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PedidoDeImpressaoForm

# View de detalhamento do pedido
from .models import PedidoDeImpressao
from django.contrib.auth.decorators import login_required

@login_required
def detalhar_pedido(request, pedido_id):
    pedido = get_object_or_404(PedidoDeImpressao, id=pedido_id, usuario=request.user)
    return render(request, 'impressoes/detalhar_pedido.html', {'pedido': pedido})

from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.db.models import Q


@login_required
def criar_pedido(request):
    if request.method == 'POST':
        form = PedidoDeImpressaoForm(request.POST, request.FILES)
        if form.is_valid():
            pedido = PedidoDeImpressao.objects.create(
                usuario=request.user,
                observacao=form.cleaned_data['observacao'],
                quantidade_documentos=form.cleaned_data['quantidade_documentos'],
                quantidade_folhas=form.cleaned_data['quantidade_folhas'],
                frente_verso=form.cleaned_data['frente_verso'],
                grampear=form.cleaned_data['grampear'],
                tipo_impressao=form.cleaned_data['tipo_impressao'],
            )
            arquivos = request.FILES.getlist('arquivos')
            for arq in arquivos:
                ArquivoPedido.objects.create(pedido=pedido, arquivo=arq)
            messages.success(request, 'Pedido de impressão enviado com sucesso!')
            return redirect('painel_professor')
        else:
            messages.error(request, 'Preencha todos os campos obrigatórios corretamente.')
    else:
        form = PedidoDeImpressaoForm()
    return render(request, 'impressoes/criar_pedido.html', {'form': form})


def is_admin(user):
    return user.is_authenticated and (hasattr(user, 'tipo') and user.tipo == 'admin')



@user_passes_test(is_admin)
def painel_admin(request):
    status = request.GET.get('status', '')
    busca = request.GET.get('q', '')
    pedidos = PedidoDeImpressao.objects.all().order_by('-data_criacao')
    if status:
        pedidos = pedidos.filter(status=status)
    if busca:
        pedidos = pedidos.filter(Q(usuario__username__icontains=busca) | Q(arquivo__icontains=busca))
    paginator = Paginator(pedidos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
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
    return render(request, 'impressoes/painel_admin.html', {'pedidos': page_obj, 'page_obj': page_obj, 'status': status, 'busca': busca})



@login_required
def painel_professor(request):
    status = request.GET.get('status', '')
    busca = request.GET.get('q', '')
    pedidos = PedidoDeImpressao.objects.filter(usuario=request.user).order_by('-data_criacao')
    if status:
        pedidos = pedidos.filter(status=status)
    if busca:
        pedidos = pedidos.filter(arquivos__arquivo__icontains=busca)
    paginator = Paginator(pedidos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        acao = request.POST.get('acao')
        pedido_id = request.POST.get('pedido_id')
        pedido = PedidoDeImpressao.objects.get(id=pedido_id, usuario=request.user)
        if acao == 'excluir':
            pedido.delete()
            messages.success(request, 'Pedido excluído!')
        return redirect('painel_professor')
    return render(request, 'impressoes/painel_professor.html', {'pedidos': page_obj, 'page_obj': page_obj, 'status': status, 'busca': busca})


