# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^usuario/', 					include('usuarios.urls', namespace='usuario')),
    url(r'^docente/', 					include('docentes.urls', namespace='docente')),
    url(r'^evaluacion/', 				include('evaluaciones.urls', namespace='evaluacion')),
    url(r'^menu/', 					 	include('menus.urls', namespace='menu')),
    url(r'^', 					 	    include('usuarios.urls', namespace='index')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
