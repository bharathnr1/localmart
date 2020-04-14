from django.db import models

from product.models import Product
# Create your models here.

class Cart(models.Model):
    product = models.ManyToManyField(Product, null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)

    def __str__(self):
        self.total = str(self.total)
        return self.total