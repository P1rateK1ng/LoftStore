from django.db import models
import uuid

class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=1000)
    product_category = models.CharField(max_length=1000)
    product_description = models.TextField(max_length=20000)
    Product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_count = models.IntegerField()
