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
        ]

        labels = {
            'nombre': 'Nombre',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'email': 'Correo Electrónico',
            'website': 'Sitio Web',
        }
