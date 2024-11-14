from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    numero_estudiantes = models.IntegerField()
    cantidad_cursos = models.IntegerField()

    def __str__(self):
        return self.nombre