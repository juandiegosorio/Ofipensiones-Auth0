from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('instituciones/', views.institucion_list),
    path('institucion/<id>', views.single_institucion, name='singleInstitucion'),
    path('institucioncreate/', csrf_exempt(views.institucion_create), name='institucionCreate'),
    path('estudiantes/', views.estudiantes_list, name='estudiantes_list'),
]
