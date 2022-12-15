from django.db import models

# Create your models here.
import uuid


class Products(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_user = models.CharField(max_length=50, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_user = models.CharField(max_length=50, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    product_name = models.CharField(max_length=100, null=True, blank=True)
    product_description = models.CharField(max_length=100, null=True, blank=True)
    status_choices = (
        ('Available', 'Available'),
        ('Out of Stock', 'Out of Stock'),

    )
    product_status = models.CharField(max_length=50, choices=status_choices)
    category_choices = (
        ('Clothing', 'Clothing'),
        ('Electronics', 'Electronics'),
        ('Vegetables', 'Vegetables'),
        ('Furniture', 'Furniture'),
        ('Medicines', 'Medicines'),

    )
    product_category = models.CharField(max_length=50, choices=category_choices)
    product_prize = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    product_image = models.ImageField(null=True, blank=True, upload_to='uploads/product_images')

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.product_name