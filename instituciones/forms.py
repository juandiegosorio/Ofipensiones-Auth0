from django import forms
from .models import Institucion

class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = [
            'nombre',
            'direccion',
            'telefono',
            'email',
            'website',
            'numero_estudiantes',
            'cantidad_cursos',
        ]

        labels = {
            'nombre': 'Nombre',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'email': 'Correo Electrónico',
            'website': 'Sitio Web',
            'numero de estudiantes': 'Número de Estudiantes',
            'cantidad de cursos': 'Cantidad de Cursos',
        }
