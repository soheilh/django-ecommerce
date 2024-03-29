from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('(?P<id>\d+)/comment', views.CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
