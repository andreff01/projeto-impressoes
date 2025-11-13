from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models_impressora import Impressora
from .forms_impressora import ImpressoraForm

@user_passes_test(lambda u: u.is_authenticated and hasattr(u, 'tipo') and u.tipo == 'admin')
def listar_impressoras(request):
    impressoras = Impressora.objects.all()
    return render(request, 'impressoes/listar_impressoras.html', {'impressoras': impressoras})

@user_passes_test(lambda u: u.is_authenticated and hasattr(u, 'tipo') and u.tipo == 'admin')
def criar_impressora(request):
    if request.method == 'POST':
        form = ImpressoraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Impressora cadastrada com sucesso!')
            return redirect('listar_impressoras')
    else:
        form = ImpressoraForm()
    return render(request, 'impressoes/form_impressora.html', {'form': form})

@user_passes_test(lambda u: u.is_authenticated and hasattr(u, 'tipo') and u.tipo == 'admin')
def editar_impressora(request, impressora_id):
    impressora = get_object_or_404(Impressora, id=impressora_id)
    if request.method == 'POST':
        form = ImpressoraForm(request.POST, instance=impressora)
        if form.is_valid():
            form.save()
            messages.success(request, 'Impressora atualizada com sucesso!')
            return redirect('listar_impressoras')
    else:
        form = ImpressoraForm(instance=impressora)
    return render(request, 'impressoes/form_impressora.html', {'form': form, 'edicao': True})

@user_passes_test(lambda u: u.is_authenticated and hasattr(u, 'tipo') and u.tipo == 'admin')
def excluir_impressora(request, impressora_id):
    impressora = get_object_or_404(Impressora, id=impressora_id)
    if request.method == 'POST':
        impressora.delete()
        messages.success(request, 'Impressora excluída com sucesso!')
        return redirect('listar_impressoras')
    return render(request, 'impressoes/confirmar_exclusao_impressora.html', {'impressora': impressora})
