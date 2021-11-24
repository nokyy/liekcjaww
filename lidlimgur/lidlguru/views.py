from django_filters import DateTimeFilter, FilterSet
from rest_framework import permissions, viewsets

from .models import Answer, Category, Comment, CustomUser, Post
from .serializers import (AnswerToCommentSerializer, CategorySerializer,
                          CommentSerializer, CustomUserSerializer,
                          SerializeTHIS)

# Create your views here.


class DateFilterPost(FilterSet):
    from_date = DateTimeFilter(field_name="date", lookup_expr="gte")
    to_date = DateTimeFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = Post
        fields = ["from_date", "to_date", "categories"]


class DateFilterComment(FilterSet):
    from_date = DateTimeFilter(field_name="date", lookup_expr="gte")
    to_date = DateTimeFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = Comment
        fields = ["from_date", "to_date"]


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-date")
    serializer_class = SerializeTHIS
    permission_classes = [permissions.IsAuthenticated]

    # filterset_fields = ['date', 'categories']
    filter_class = DateFilterPost
    search_fields = ["author__username", "title"]
    ordering_fields = ["author", "title", "date"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-date")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    # filterset_fields = ['date']
    filter_class = DateFilterComment
    search_fields = ["author__username", "Post__title", "content"]
    ordering_fields = ["author", "Post", "date"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AnswerToCommentViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by("-comment")
    serializer_class = AnswerToCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    search_fields = ["author__username", "comment__Post", "content"]
    ordering_fields = ["author", "comment"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CustomUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
