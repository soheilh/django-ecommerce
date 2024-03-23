from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    category = serializers.StringRelatedField(many=True)

    def get_description(self, obj):
        return obj.description[:100]

    class Meta:
        model = Post
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        fields = (
            "title",
            "slug",
            "thumb",
            "category",
            "description",
            "publish",
        )

class PostDetailSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True)
    class Meta:
        model = Post
        fields = '__all__'