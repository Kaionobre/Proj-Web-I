from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages  # para exibir mensagens ao usuário

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        usuario = authenticate(email=email, password=senha)

        if usuario:
            login(request, usuario)
            messages.success(request, 'Você entrou com sucesso!')  
            return redirect('home')  
        else:
            messages.error(request, 'ERRO: Login inválido. Verifique seu e-mail e senha.')
            return render(request, 'accounts/pages/login.html')
    else:
        return render(request, 'accounts/pages/login.html')

def cadastro(request):
    if request.method == "POST":
        nome = request.POST.get('nome')  
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        usuario = User.objects.filter(email=email).first()

        if usuario:
            messages.error(request, 'Já existe um usuário com este e-mail.')
            return render(request, 'accounts/pages/cadastro.html')

        usuario = User.objects.create_user(username=email, email=email, password=senha)
        usuario.save()

        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login')  

    else:
        return render(request, 'accounts/pages/cadastro.html')

def logout(request):
    logout(request)
    messages.success(request, 'Você saiu com sucesso.')
    return redirect('login')  
