from django.db import models

# Create your models here.

class Branch(models.Model):
    name= models.CharField(max_length=100)
    department= models.CharField(max_length=100)

class Country(models.Model):
    name= models.CharField(max_length=100)

class CustomerType(models.Model):
    name= models.CharField(max_length=100)

class Gender(models.Model):
    name= models.CharField(max_length=100)

class ProductLine(models.Model):
    name= models.CharField(max_length=100)

class Payment(models.Model):
    name= models.CharField(max_length=100)
    category= models.CharField(max_length=100)

class SuperMarketSales(models.Model):
    unit_price = models.DecimalField(max_digits=100, decimal_places=2)
    quantity = models.IntegerField()
    date = models.DateField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    customer_type = models.ForeignKey(CustomerType, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    product_line= models.ForeignKey(ProductLine, on_delete=models.CASCADE)
    payment= models.ForeignKey(Payment, on_delete=models.CASCADE)
    