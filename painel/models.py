from django.db import models


class Painel(models.Model):
    objects = None
    quarto = models.CharField(max_length=2, blank=True)
    pessoas = models.CharField(max_length=1, blank=True)
    texto = models.TextField()
    
    def __str__(self) -> str:
        return self.texto
