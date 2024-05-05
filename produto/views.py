from django.http import HttpResponse
from django.shortcuts import render
from .models import Produto

def home(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/pages/home.html', {'produtos': produtos})

def categoria(request, categoria):
    produtos = Produto.objects.filter(categoria=categoria)
    return render(request, 'produtos/pages/categoria.html', {'produtos': produtos, 'categoria': categoria})


