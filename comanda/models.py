from django.db import models


class Comanda(models.Model):
    objects = None
    quarto = models.CharField(max_length=2, blank=True)
    descricao = models.CharField(max_length=50, blank=True)
    quantidade = models.CharField(max_length=2, blank=True)
    valor_total = models.CharField(max_length=8, blank=True)
    valor_unitario = models.CharField(max_length=8, blank=True)
    datahora = models.CharField(max_length=10, blank=True)
    valor_quarto = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.descricao
