from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('product', views.ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
]
