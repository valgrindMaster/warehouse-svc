from rest_framework import serializers
from shop.models import Category, Inventory, Product


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['product', 'quantity_in_stock']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    quantity_in_stock = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image_url', 'quantity_in_stock']

    def get_quantity_in_stock(self, obj):
        """Fetch inventory quantity for the given product."""
        try:
            return obj.inventory.quantity_in_stock
        except Inventory.DoesNotExist:
            return 0