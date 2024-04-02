from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Post, Comment
from .serializer import PostSerializer, PostDetailSerializer, CommentSerializer

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

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        post_id = kwargs.get('id')
        data['post'] = post_id
        data['user'] = request.user.id

        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        post_slug = self.kwargs.get('slug')
        post = Post.objects.filter(slug=post_slug).first()
        if post:
            post_id = post.id
            queryset = Comment.objects.filter(post_id=post_id)
            return queryset
        else:
            raise NotFound() # Return an not found message if post is not found.