# Generated by Django 4.1.4 on 2022-12-15 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_products_product_prize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.FileField(blank=True, null=True, upload_to='uploads/product_images'),
        ),
    ]
