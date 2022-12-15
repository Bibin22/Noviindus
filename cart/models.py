from django.db import models
import uuid
from django.contrib.auth.models import User


class Cart(models.Model):
    cart_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_user = models.CharField(max_length=50, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_user = models.CharField(max_length=50, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, models.CASCADE, null=True, blank=True)
    product = models.ForeignKey('products.Products', models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.product)
