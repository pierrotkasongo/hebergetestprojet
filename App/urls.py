from django.urls import path, include
from .views import *

urlpatterns = [
   path('',home, name='home'),
   path('update_product/id=<int:id>', update_product, name='update_product'),
   path('delete_product/id=<int:id>', delete_product, name='delete_product'),
]