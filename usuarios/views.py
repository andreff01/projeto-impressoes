from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.views import LoginView

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['senha']
        user = authenticate(request, username=username, password=senha)
        if user is not None:
            login(request, user)
            if user.tipo == 'professor':
                return redirect('/painel_professor/')
            elif user.tipo == 'admin':
                return redirect('/painel_admin/')
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')



from .forms import UsuarioCreationForm

def registro_view(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado com sucesso!')
            return redirect('login')
    else:
        form = UsuarioCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def painel_admin(request):
    return HttpResponse("Bem-vindo, Administrador!")

from django.contrib import messages

class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'

    def form_invalid(self, form):
        messages.error(self.request, 'Usuário ou senha inválidos, ou tipo de usuário não definido.')
        return super().form_invalid(form)

    def get_success_url(self):
        user = self.request.user
        if hasattr(user, 'tipo') and user.tipo:
            if user.tipo == 'professor':
                return '/impressoes/meus-envios/'
            elif user.tipo == 'admin':
                return '/impressoes/painel/'
        messages.error(self.request, 'Seu perfil não possui tipo definido. Contate o administrador.')
        return '/usuarios/login/'