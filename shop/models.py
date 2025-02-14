from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image_url = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    quantity_in_stock = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        return f"{self.product.name} - {self.quantity_in_stock} in stock"
