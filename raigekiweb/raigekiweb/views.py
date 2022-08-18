from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def product_detail(request):
    return render(request, 'product-details.html')

def shop(request):
    return render(request, 'shop.html')

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