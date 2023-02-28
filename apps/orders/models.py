from django.db import models
from ..users.models import User
from ..products.models import Product
import uuid

class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    order_price = models.DecimalField(max_digits=9, decimal_places=2)

class OrderedProduct(models.Model):
    op_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    op_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    op_count = models.IntegerField()