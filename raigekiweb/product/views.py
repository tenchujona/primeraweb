from django.shortcuts import render
from products.models import Products

# Create your views here.
def products(request):

    context = {}
    return render(request, 'productos.html', context=context)