from django.http import HttpResponse
from datetime import datetime

def saludo(request):
    return HttpResponse('Hola buenas tardes!')


def tienda(request):
    return HttpResponse('Esta es la tienda')

def despedida(request):
    return HttpResponse('Hasta luego gracias por visitar nuestra web')

def nosotros(request):
    return HttpResponse('Pagina acerca de nosotros')

def fecha_actual(request):
    fecha = datetime.now().date()
    mensaje = f'Hoy es {fecha}'
    return HttpResponse(mensaje)