from django.db import models


class Caixa(models.Model):
    objects = None
    data = models.CharField(max_length=10, blank=True)
    entrada = models.CharField(max_length=10, blank=True)
    usuario = models.CharField(max_length=20, blank=True)
    total = models.CharField(max_length=10, blank=True)
    saida = models.CharField(max_length=10, blank=True)
    
    def __str__(self) -> str:
        return self.data