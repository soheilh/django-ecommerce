from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Product, Comment
from .serializers import ProductSerializer, ProductDetailSerializer, CommentSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ProductSerializer
        elif self.action == "retrieve":
            return ProductDetailSerializer
        return self.serializer_class

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        product_id = kwargs['id']
        data['product'] = product_id
        data['user'] = request.user.id

        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        product_id = self.kwargs['id']
        queryset = Comment.objects.filter(product_id=product_id)
        return queryset
    
