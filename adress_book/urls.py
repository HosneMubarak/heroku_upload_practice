from django.urls import path
from .views import home, add_address, editView, deleteView

urlpatterns = [
    path('', home, name='home'),
    path('address/', add_address, name='add-address'),
    path('edit/<list_id>/', editView, name='edit-address'),
    path('delete/<list_id>', deleteView, name='delete-address'),
]
