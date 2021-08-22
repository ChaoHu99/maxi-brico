from django.urls import path
from myapps.principal.views import list_all_products, show_product, get_stripe_pub_key


urlpatterns = [
    path('products/', list_all_products, name = 'list_all_products'),
]