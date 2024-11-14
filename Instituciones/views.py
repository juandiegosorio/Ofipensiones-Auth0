from django.shortcuts import render
from .forms import InstitucionForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .logic.logic_measurement import crear_institucion, get_instituciones
from django.contrib.auth.decorators import login_required
#from monitoring.auth0backend import getRole

@login_required
def institucion_list(request):
    role = getRole(request)
    if role == "Administrador Ofipensiones":
        instituciones = get_instituciones()
        context = {
            'institucion_list': instituciones
        }
        return render(request, 'Institucion/instituciones.html', context)
    else:
        return HttpResponse("Unauthorized User")

def institucion_create(request):
    role = getRole(request)
    if role == "Administrador Ofipensiones":
        if request.method == 'POST':
            form = InstitucionForm(request.POST)
            if form.is_valid():
                crear_institucion(form)
                messages.add_message(request, messages.SUCCESS, 'Institución creada con éxito')
                return HttpResponseRedirect(reverse('institucionCreate'))
            else:
                print(form.errors)
        else:
            form = InstitucionForm()
        context = {
            'form': form,
        }

        return render(request, 'Institucion/institucionCreate.html', context)
    else:
        return HttpResponse("Unauthorized User")