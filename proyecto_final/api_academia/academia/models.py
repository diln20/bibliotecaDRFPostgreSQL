from django.db import models

class Programa(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=120, unique=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f'{self.codigo} - {self.nombre}'


class Estudiante(models.Model):
    nombre = models.CharField(max_length=120)
    correo = models.EmailField(unique=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, db_index=True)
    programa = models.ForeignKey(
        Programa,
        on_delete=models.PROTECT,
        related_name='estudiantes',
    )

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} - {self.correo}'
