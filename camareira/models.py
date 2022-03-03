from django.db import models


class Camareira(models.Model):
    objects = None
    nome = models.CharField(max_length=100, blank=True)
    codigo = models.CharField(max_length=3, blank=True)

    def __str__(self):
        return self.nome
