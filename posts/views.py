
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from posts.models import Post
from posts.serializers import PostSerializer, PostCreateSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from users.permissions import IsAuthor


class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (AllowAny,)


class PostDetailAPIView(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (AllowAny,)


class PostCreateAPIView(CreateAPIView):
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAdminUser | IsAuthenticated,)

    def perform_create(self, serializer):
        post = serializer.save()
        post.author = self.request.user
        post.save()


class PostUpdateAPIView(UpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAdminUser | IsAuthor,)


class PostDeleteAPIView(DestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAdminUser | IsAuthor,)
