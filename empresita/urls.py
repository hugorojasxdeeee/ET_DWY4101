"""empresita URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from apps.clientes.views import formulario_view,index,cliente_list
from apps.orden.views import orden_view,orden_list
from apps.tecnico.views import tecnico_view,tecnico_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^registro/', formulario_view, name='registro'),
    url(r'^crear/', orden_view, name='crear'),
    url(r'^registrar/', tecnico_view, name='registrar'),
    url(r'^listar/', tecnico_list, name='listar'),
    url(r'^inicio/', index, name='inicio'),
    url(r'^lista/', cliente_list, name='lista'),
    url(r'^order_lista/', orden_list, name='order_lista'),
    url(r'^accounts/', include('allauth.urls')),
]
