from django.db import models

class Seller(models.Model):
    mobile_number = models.CharField(max_length=20, unique=True)
    otp = models.CharField(max_length=6, null=True)


    def __str__(self):
        return self.mobile_number

class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    link = models.CharField(max_length=100, unique=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
