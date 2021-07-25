from django.db import models

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

    def __str__(self):
        return '{} ({})'.format(self.name, self.barcode)
