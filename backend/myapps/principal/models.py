from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
User = settings.AUTH_USER_MODEL

class Product(models.Model):

    barcode = models.PositiveBigIntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null = True)
    SECTIONS = (('General', 'General'),
        ('Ferreteria', 'Ferreteria'),
        ('Vehiculos', 'Vehiculos'),
        ('Hogar', 'Hogar'),
        ('Verano', 'Verano'),
        ('Navidad', 'Navidad'),
        ('Juguetes', 'Juguetes'),
        ('Papeleria', 'Papeleria'),
        ('Manualidades', 'Manualidades'),
        ('Fiesta', 'Fiesta'),
        ('Marcos', 'Marcos'),
        ('Baño', 'Baño'),
        ('Cocina', 'Cocina'),
        ('Lanas', 'Lanas'),
        ('Maquillaje', 'Maquillaje'),
        ('Mascotas', 'Mascotas'),
        ('Jardineria', 'Jardineria'),
        ('Higiene', 'Higiene'),
        ('Limpieza', 'Limpieza'),
        ('Plasticos', 'Plasticos'))
    
    section = models.TextField(choices=SECTIONS, default='General')
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=50, blank=True, null = True, default='Estándard')
    colour = models.CharField(max_length=20, blank=True, null = True, default='Estándard')
    stock = models.PositiveIntegerField()
    image = models.URLField()
    brand = models.CharField(max_length=50, blank=True, null = True)
    client_price = models.DecimalField(max_digits=10, decimal_places=2, default=1.0)

    def __str__(self):
        return '{} ({})'.format(self.name, self.barcode)

class Order(models.Model):
    PLAN_ACTIVE = 'active'
    PLAN_CANCELLED = 'cancelled'

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    products = models.ManyToManyField(Product, related_name='products')
    creation_date = models.DateTimeField(auto_now_add=True)
    DELIVERY_STATUS = (('Preparación', 'Preparación'),
        ('En proceso', 'En proceso'),
        ('Entregado', 'Entregado'),
        ('Rechazado', 'Rechazado'))
    delivery_status = models.TextField(choices=DELIVERY_STATUS, default='Preparación', null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    address = models.TextField(default='Recoger en la tienda')

   
