from django.http import HttpResponse
from django.shortcuts import render
from .models import Produto
from django.contrib.auth.decorators import login_required


def home(request):
    nome_cliente = request.user.username
    produtos = Produto.objects.all()
    return render(request, 'produtos/pages/home.html', {'produtos': produtos,'nome_cliente': nome_cliente})

def categoria(request, categoria):
    produtos = Produto.objects.filter(categoria=categoria)
    return render(request, 'produtos/pages/categoria.html', {'produtos': produtos, 'categoria': categoria})


