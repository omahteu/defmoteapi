from django.db import models


class Cabeca(models.Model):
    objects = None
    datahora = models.CharField(max_length=10, blank=True)
    valor = models.CharField(max_length=10, blank=True)
    quarto = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return self.quarto
