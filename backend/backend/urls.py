"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapps.users.views import Login, Logout
from myapps.principal.views import show_product, get_stripe_pub_key, create_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', include('myapps.principal.urls')),
    path('login/', Login.as_view(), name = 'Login'),
    path('logout/', Logout.as_view(), name = 'Logout'),
    path('create/', include('myapps.users.urls')),
    path('stripe/get-stripe-pub-key/', get_stripe_pub_key, name = 'get_stripe_pub_key'),
    path('product/<int:pk>/', show_product, name = 'show_product'),
    path('create/order/', create_order, name = 'create_order'),
]
