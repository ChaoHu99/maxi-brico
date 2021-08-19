from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    size = models.CharField(max_length=50, blank=True, null = True)
    colour = models.CharField(max_length=20, blank=True, null = True)
    stock = models.PositiveIntegerField()
    image = models.URLField()
    brand = models.CharField(max_length=50, blank=True, null = True)
    client_price = models.DecimalField(max_digits=10, decimal_places=2, default=1.0)

    def __str__(self):
        return '{} ({})'.format(self.name, self.barcode)

   
