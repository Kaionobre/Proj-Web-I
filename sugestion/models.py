from django.db import models

# Create your models here.

class Sugestion(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    #image = models.imageField()