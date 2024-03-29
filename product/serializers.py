from rest_framework import serializers
from .models import Product, Picture, Comment

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()

    def get_picture(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pictures.first().file.url)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'picture',
            'price',
            'offer',
            'count_sold',
            'category',
            'color',
            'brand',
                  )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'