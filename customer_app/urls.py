from django.urls import path
from . import views

urlpatterns = [
    path('create_customer/', views.create_customer),
    path('get_store_details/', views.get_store_details),
    path('add_to_cart/', views.add_to_cart),
    path('place_order/', views.place_order),
]
