from django.db import models


class Painel(models.Model):
    objects = None
    texto = models.TextField()
    
    def __str__(self) -> str:
        return self.texto
