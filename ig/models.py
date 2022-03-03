from django.db import models


class Ig(models.Model):
    objects = None
    social = models.CharField(max_length=200, blank=True)
    fantasia = models.CharField(max_length=200, blank=True)
    cnpj = models.CharField(max_length=14, blank=True)
    cidade = models.CharField(max_length=50, blank=True)
    endereco = models.CharField(max_length=200, blank=True)
    numero = models.CharField(max_length=5, blank=True)
    bairro = models.CharField(max_length=50, blank=True)
    telefone = models.CharField(max_length=11, blank=True)
    telefone2 = models.CharField(max_length=11, blank=True)
    telefone3 = models.CharField(max_length=11, blank=True)

    def __str__(self):
        return self.fantasia
