from django.urls import path
from myapps.principal.views import list_all_products, show_product


urlpatterns = [
    path('products/', list_all_products, name = 'list_all_products'),
    path('product/<int:pk>/', show_product, name = 'show_product'),
]