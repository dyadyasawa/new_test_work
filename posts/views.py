
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser,)


class PostDetailAPIView(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser,)


class PostCreateAPIView(CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser,)


class PostUpdateAPIView(UpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAdminUser,)


class PostDeleteAPIView(DestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAdminUser,)
