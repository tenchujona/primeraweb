"""raigekiweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from raigekiweb.views import saludo, tienda, index, nosotros, fecha_actual, probando_template
from product.views import products
urlpatterns = [
    path('', index, name = 'home'),
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name = 'saludo'),
    path('tienda/', tienda, name = 'tienda'),
    path('index/', index, name = 'home'),
    path('nosotros/', nosotros, name = 'nosotros'),
    path('fechadehoy/', fecha_actual, name = 'fecha'),
    path('probandotemplate/', probando_template, name = 'probandotemplate'),
    path('products/', include('product.urls'))
]
