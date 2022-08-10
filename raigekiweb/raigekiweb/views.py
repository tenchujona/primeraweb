from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def saludo(request):
    return HttpResponse('Hola buenas tardes!')


def tienda(request):
    return HttpResponse('Esta es la tienda')

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return HttpResponse('Pagina acerca de nosotros')

def fecha_actual(request):
    fecha = datetime.now().date()
    mensaje = f'Hoy es {fecha}'
    return HttpResponse(mensaje)

def probando_template(request):
    context = {'nombre':'Jona',
               'apellido':'Otero',
               'frutas':['banana', 'manzana'],
                }
    return render(request, 'template.html', context = context)