from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    preco = models.FloatField(null=False, blank=False)
    estoque = models.IntegerField(null=False, blank=False)
    marca = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False)
    
    def __str__(self):
        return self.nome