from django.shortcuts import render, redirect
from .models import Impressao
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

@login_required
def enviar_impressao(request):
    if request.method == 'POST':
        arquivo = request.FILES.get('arquivo')
        quantidade = request.POST.get('quantidade_folhas')
        frente_verso = request.POST.get('frente_verso') == 'on'
        grampear = request.POST.get('grampear') == 'on'
        tipo = request.POST.get('tipo_impressao')

        if not arquivo or not quantidade or not tipo:
            messages.error(request, 'Preencha todos os campos obrigatórios!')
        else:
            Impressao.objects.create(
                usuario=request.user,
                arquivo=arquivo,
                quantidade_folhas=int(quantidade),
                frente_verso=frente_verso,
                grampear=grampear,
                tipo_impressao=tipo,
            )
            messages.success(request, 'Arquivo enviado com sucesso!')
            return redirect('enviar_impressao')

    return render(request, 'impressoes/enviar.html')

def is_admin(user):
    return user.is_authenticated and user.tipo == 'admin'

@user_passes_test(is_admin)
def painel_admin(request):
    impressoes = Impressao.objects.all().order_by('-criado_em')

    if request.method == 'POST':
        impressao_id = request.POST.get('id')
        campo = request.POST.get('campo')
        valor = request.POST.get('valor') == 'true'

        impressao = Impressao.objects.get(id=impressao_id)
        setattr(impressao, campo, valor)
        impressao.save()
        messages.success(request, f'{campo} atualizado com sucesso!')

    return render(request, 'impressoes/painel_admin.html', {'impressoes': impressoes})

@login_required
def painel_professor(request):
    impressoes = Impressao.objects.filter(usuario=request.user)
    return render(request, 'impressoes/painel_professor.html', {'impressoes': impressoes})


