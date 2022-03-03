from django.db import models


class Emeil(models.Model):
    objects = None
    usuario = models.CharField(max_length=100, blank=True)
    senha = models.CharField(max_length=20, blank=True)
    smtp = models.CharField(max_length=50, blank=True)
    porta = models.CharField(max_length=10, blank=True)
    timeout = models.CharField(max_length=2, blank=True)
    email_destino = models.CharField(max_length=100, blank=True)
    email_contabilidade = models.CharField(max_length=100, blank=True)
    autenticacao = models.BooleanField()

    def __str__(self):
        return self.usuario
