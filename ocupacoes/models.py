from django.db import models


class Ocupacao(models.Model):
    objects = None
    data = models.CharField(max_length=10, blank=True)
    codigo = models.CharField(max_length=10, blank=True)
    quarto = models.CharField(max_length=5, blank=True)
    entrada = models.CharField(max_length=10, blank=True)
    saida = models.CharField(max_length=10, blank=True)
    total = models.CharField(max_length=10, blank=True)
    
    def __str__(self) -> str:
        return self.codigo
