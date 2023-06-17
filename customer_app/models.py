from django.db import models

class Customer(models.Model):
    mobile_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    store = models.ForeignKey('seller_app.Store', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('seller_app.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
