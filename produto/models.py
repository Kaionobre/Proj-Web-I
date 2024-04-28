from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.CharField(max_length=15)
    tamanho = models.CharField(max_length=5)
    descricao = models.TextField()
    #image = models.imageField()


