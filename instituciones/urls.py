from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('instituciones/', views.institucion_list),
    path('institucioncreate/', csrf_exempt(views.institucion_create), name='institucionCreate'),
]