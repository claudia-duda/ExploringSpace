from django.contrib import messages
from django.shortcuts import redirect, render
from usuarios.forms import CadastroForms, LoginForms
from django.contrib import auth
from django.contrib.auth.models import User


def login (request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():

            nome = form["nome_login"].value()
            senha = form["senha"].value()

            usuario = auth.authenticate(
                request,
                username = nome,
                password = senha
            )

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f"Bem vindo(a) {nome}")
                return redirect('index')
            else:
                messages.error(request, "Erro ao realizar ao login")
                return redirect('login')

    return render(request, "usuarios/login.html", {"form" : form })

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():

            nome = form["nome_cadastro"].value()
            email = form["email"].value()
            senha = form["senha_inicial"].value()

            if User.objects.filter(username = nome).exists():
                messages.error(request, "Usuario já cadastrado")
                return redirect('cadastro')

            if senha != form["senha_confirmar"].value():
                messages.error(request, "Senhas não são iguais")
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username = nome,
                email = email,
                password = senha
            )
            usuario.save()
            messages.success(request, f"Usuario {nome} criado com sucesso!")
            return redirect('login')

    return render(request, "usuarios/cadastro.html", { "form" : form })