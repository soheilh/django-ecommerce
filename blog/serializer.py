from rest_framework import serializers
from .models import Post, Comment

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

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        read_only_fields = ('user', 'depth',)
        fields = '__all__'

    def validate_depth(self, value):
        if value is None:
            return value
        if value.depth >= 2:
            raise serializers.ValidationError("Maximum depth of comments reached.")
        return value
    
    def create(self, validated_data):
        parent = validated_data.get('parent', None)
        if parent:
            validated_data['depth'] = parent.depth + 1
        return super().create(validated_data)