from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('', views.PostViewSet, basename='posts')
router.register('(?P<slug>[-\w]+)/comments', views.CommentViewSet, basename='post-comments')

urlpatterns = [
    path('', include(router.urls)),
]
