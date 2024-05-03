from django.http import HttpResponse
from django.shortcuts import render
from .models import Produto

def home(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/pages/home.html', {'produtos': produtos})




