from rest_framework import serializers
from .models import Product

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'offer',
            'count_sold',
            'category',
            'color',
            'brand',
                  )