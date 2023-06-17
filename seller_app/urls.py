from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.seller_signup),
    path('create_store/', views.create_store),
    path('upload_product/', views.upload_product),
]
