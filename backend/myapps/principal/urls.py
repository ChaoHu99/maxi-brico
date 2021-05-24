from django.urls import path
from myapps.principal.views import list_all_products

urlpatterns = [
    path('products/', list_all_products, name = 'list_all_products'),
]