
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from comments.models import Comment
from comments.serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from users.permissions import IsAuthor


class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (AllowAny, IsAdminUser,)


class CommentDetailAPIView(RetrieveAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (AllowAny, IsAdminUser,)


class CommentCreateAPIView(CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser,)

    def perform_create(self, serializer):
        comment = serializer.save()
        comment.author = self.request.user
        comment.save()


class CommentUpdateAPIView(UpdateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAdminUser, IsAuthor,)


class CommentDeleteAPIView(DestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAdminUser, IsAuthor,)
