
from django.urls import path

from comments.apps import CommentsConfig
from comments.views import (
    CommentListAPIView,
    CommentDetailAPIView,
    CommentCreateAPIView,
    CommentUpdateAPIView,
    CommentDeleteAPIView
)

app_name = CommentsConfig.name

urlpatterns = [
    path("list/", CommentListAPIView.as_view(), name="comment-list"),
    path("detail/<int:pk>/", CommentDetailAPIView.as_view(), name="comment-detail"),
    path("create/", CommentCreateAPIView.as_view(), name="comment-create"),
    path("update/<int:pk>/", CommentUpdateAPIView.as_view(), name="comment-update"),
    path("delete/<int:pk>/", CommentDeleteAPIView.as_view(), name="comment-delete"),
]
