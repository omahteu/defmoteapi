from django.db import models


class Quarto(models.Model):
    objects = None
    codigo = models.CharField(max_length=5, blank=True)
    numero = models.CharField(max_length=2, blank=True)
    horas_locacao = models.CharField(max_length=2, blank=True)
    valor_locacao = models.CharField(max_length=8, blank=True)
    tempo_especial = models.CharField(max_length=2, blank=True)
    valor_especial = models.CharField(max_length=8, blank=True)
    horas_diaria = models.CharField(max_length=2, blank=True)
    valor_diaria = models.CharField(max_length=8, blank=True)
    tempo_adicional = models.CharField(max_length=2, blank=True)
    valor_adicional = models.CharField(max_length=2, blank=True)
    tolerancia = models.CharField(max_length=2, blank=True)
    tipo_quarto = models.CharField(max_length=30, blank=True)
    tipo_tabela = models.CharField(max_length=10, blank=True)
    percentual = models.BooleanField()
    vh1 = models.CharField(max_length=8, blank=True)
    vh2 = models.CharField(max_length=8, blank=True)
    vh3 = models.CharField(max_length=8, blank=True)
    vh4 = models.CharField(max_length=8, blank=True)
    vh5 = models.CharField(max_length=8, blank=True)
    vh6 = models.CharField(max_length=8, blank=True)

    def __str__(self):
        return self.numero
