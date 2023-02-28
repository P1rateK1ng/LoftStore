from django.db import models
import uuid

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    email = models.CharField(max_length=320)
    password = models.CharField(max_length=50)
    shipping_adress = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=20)