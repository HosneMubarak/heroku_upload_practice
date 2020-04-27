from django.urls import path
from .views import home, add_address

urlpatterns = [
    path('', home, name='home'),
    path('address/', add_address, name='add-address'),
]
