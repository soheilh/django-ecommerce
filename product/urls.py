from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('products/(?P<id>\d+)/comments', views.CommentViewSet, basename='comments')
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('brands', views.BrandViewSet, basename='brands')
router.register('colors', views.ColorViewSet, basename='colors')

urlpatterns = [
    path('', include(router.urls)),
]
