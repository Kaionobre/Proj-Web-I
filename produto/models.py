from django.db import models
from cliente.models import Cliente
# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.CharField(max_length=15)
    image = models.ImageField(upload_to='produto/', null=True, blank=True)
    tamanho = models.CharField(max_length=5)
    categoria = models.CharField(max_length=65, null=True)

    def __str__(self):
        return self.nome

class Carrinho(models.Model):
    usuario = models.ForeignKey(Cliente, on_delete=models.CASCADE)
