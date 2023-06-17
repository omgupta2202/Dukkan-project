from django.urls import path, include

urlpatterns = [
    path('seller/', include('seller_app.urls')),
    path('customer/', include('customer_app.urls')),
]
