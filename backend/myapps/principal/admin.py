from django.contrib import admin
from myapps.principal.models import Product, Profile, Address

# Register your models here.
admin.site.register(Product)

admin.site.register(Profile)
admin.site.register(Address)