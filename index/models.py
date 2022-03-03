from django.db import models


class Dados(models.Model):
    objects = None
    nome = models.CharField(max_length=50, blank=True)
    idade = models.CharField(max_length=2, blank=True)
    
    def __str__(self) -> str:
        return self.nome
