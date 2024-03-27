from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer

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
