from rest_framework import viewsets
from .models import Post
from .serializer import PostSerializer, PostDetailSerializer

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return PostSerializer
        elif self.action == "retrieve":
            return PostDetailSerializer
        return self.serializer_class
    
    search_fields = ['title', 'description']
    lookup_field = 'slug'
