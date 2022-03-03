from django.db import models


class Patio(models.Model):
    objects = None
    quarto = models.CharField(max_length=2, blank=True)
    veiculo = models.CharField(max_length=100, blank=True)
    modelo = models.CharField(max_length=100, blank=True)
    placa = models.CharField(max_length=7, blank=True)

    def __str__(self):
        return self.quarto
