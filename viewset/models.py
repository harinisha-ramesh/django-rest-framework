from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=250, null = True)
    price = models.DecimalField(max_digits=10, decimal_places=3, null = True)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.name