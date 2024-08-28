
from django.urls import path

from posts.apps import PostsConfig
from posts.views import PostListAPIView, PostDetailAPIView, PostCreateAPIView, PostUpdateAPIView, PostDeleteAPIView

app_name = PostsConfig.name

urlpatterns = [
    path("list/", PostListAPIView.as_view(), name="post-list"),
    path("detail/<int:pk>/", PostDetailAPIView.as_view(), name="post-detail"),
    path("create/", PostCreateAPIView.as_view(), name="post-create"),
    path("update/<int:pk>/", PostUpdateAPIView.as_view(), name="post-update"),
    path("delete/<int:pk>/", PostDeleteAPIView.as_view(), name="post-delete"),
]
