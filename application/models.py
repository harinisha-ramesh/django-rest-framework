from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=250,null=True)
    product_code = models.CharField(max_length=200,null=True)
    price = models.FloatField(default=0)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.product_name