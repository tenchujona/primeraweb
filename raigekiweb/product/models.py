from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='product', null=True, blank=True)
    SKU = models.CharField(max_length=30, unique=True, blank=True, null=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

class Categorias(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'