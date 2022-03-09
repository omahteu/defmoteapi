from django.db import models


class Usuario(models.Model):
    obsjects = None
    nome = models.CharField(max_length=20, blank=True)
    senha = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10, blank=True)
    
    def __str__(self) -> str:
        return self.nome
