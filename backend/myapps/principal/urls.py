from django.urls import path
from myapps.principal.views import list_all_products, list_orders


urlpatterns = [
    path('products/', list_all_products, name = 'list_all_products'),
    path('orders/', list_orders, name = 'list_orders'),

]