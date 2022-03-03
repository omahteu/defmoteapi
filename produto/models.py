from django.db import models


class Produto(models.Model):
    objects = None
    codigo = models.CharField(max_length=5, blank=True)
    descricao = models.CharField(max_length=100, blank=True)
    valorunitario = models.CharField(max_length=8, blank=True)
    quantidade = models.CharField(max_length=5, blank=True)
    categoria = models.CharField(max_length=50, blank=True)
    data = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.descricao
