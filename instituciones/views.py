from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from monitoring.auth0backend import getRole

import requests
from django.shortcuts import render

@login_required
def estudiantes_list(request):
    # Hacemos una solicitud GET a la API
    url = "http://34.55.214.111/estudiantes/list/"
    response = requests.get(url)

    # Comprobamos que la solicitud fue exitosa
    if response.status_code == 200:
        estudiantes = response.json()  # Asumimos que la respuesta es JSON
    else:
        estudiantes = []  # En caso de error, podemos enviar una lista vacía

    # Pasamos los datos a la plantilla
    return render(request, 'estudiantes_list.html', {'estudiantes': estudiantes})

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
@login_required 
def single_institucion(request, id=0):
    role = getRole(request)
    if role == "Administrador Ofipensiones":
        institucion = get_institucion(id)
        context = {
            'institucion': institucion
        }
        return render(request, 'Institucion/institucion.html', context)
    else:
        return HttpResponse("Unauthorized User")

@login_required
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
