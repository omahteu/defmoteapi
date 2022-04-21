from django.db import models


class Debito(models.Model):
    objects = None
    bandeira = models.CharField(max_length=50, blank=True)
    porcentagem = models.CharField(max_length=2, blank=True)
    
    def __str__(self) -> str:
        return self.bandeira
