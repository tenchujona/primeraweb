from django.urls import path
from product.views import products

urlpatterns = [
    path('shop.html', products, name = 'productos'),

]
