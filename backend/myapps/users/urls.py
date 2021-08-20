from django.urls import path
from myapps.users.views import user_api_view


urlpatterns = [
    path('user/', user_api_view, name = 'create_user'),
]