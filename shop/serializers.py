from rest_framework import serializers
from shop.models import Category, Inventory, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image_url']

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['product', 'quantity_in_stock']