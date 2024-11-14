from ..models import Institucion

def get_instituciones():
    queryset = Institucion.objects.all().order_by('-nombre')
    return (queryset)

def crear_institucion(form):
    institucion = form.save()
    institucion.save()
    return ()