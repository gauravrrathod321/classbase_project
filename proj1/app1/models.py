from django.db import models

# Create your models here.
class Product(models.Model):
    payment_choice = [('On','Online'),("COD","cash on delivery")]
    product_name = models.CharField(max_length=20)
    product_price = models.IntegerField()
    product_quan = models.IntegerField()
    delivery_address= models.CharField(max_length=20)
    payment_mode = models.CharField(max_length=10,choices=payment_choice)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)