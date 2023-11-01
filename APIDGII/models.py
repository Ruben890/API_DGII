from django.db import models


class RNC(models.Model):
    rnc = models.CharField(max_length=11, null=False, blank=False)
    nombre_apellido = models.CharField(max_length=100)
    actividad_economica = models.CharField(max_length=255, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=50)
    tipo_contribuyente = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre_apellido}({self.rnc})'