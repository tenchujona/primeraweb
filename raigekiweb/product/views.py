from django.shortcuts import render
from product.models import Products

# Create your views here.
def products(request):
    productos = Products.objects.all()
    context = {'productos':productos}
    return render(request, 'productos.html', context=context)