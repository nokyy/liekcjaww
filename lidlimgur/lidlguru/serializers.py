from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Answer, Category, Comment, Post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'avatar']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

    def to_representation(self, instance):
        return instance.name


class SerializeTHIS(serializers.ModelSerializer):
    # Zakomentuj categories jak chcesz dodać post za pomocą html XD
    # odkomentuj jak chcesz widzieś w get jsonie nazwę kategorii zamiast pk_id
    # categories = CategorySerializer(many=True)
    # Odkryłem piękną rzecz zwaną slug related field
    # all hail slug related field
    categories = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field='name', many=True)
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'categories', 'author']

    def create(self, validated_data):
        author = validated_data['author']
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(read_only=True)
    Post = serializers.SlugRelatedField(
        queryset=Post.objects.all(), slug_field='title')

    class Meta:
        model = Comment
        fields = ['content', 'Post', 'author']

    def create(self, validated_data):
        author = validated_data['author']
        return super().create(validated_data)


class AnswerToCommentSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(read_only=True)
    comment = serializers.SlugRelatedField(
        queryset=Comment.objects.all(), slug_field='content')

    class Meta:
        model = Answer
        fields = ['content', 'comment', 'author']

    def create(self, validated_data):
        author = validated_data['author']
        return super().create(validated_data)
