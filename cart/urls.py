from django.urls import path
from .views import *
urlpatterns = [
    path('home', home, name='home'),
    path('add_to_cart/<str:pk>', add_to_cart, name='add_to_cart'),
    path('cart_list', cart_list, name='cart_list'),
    path('remove_from_cart/<str:pk>', remove_from_cart, name='remove_from_cart')
]