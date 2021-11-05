from rest_framework import serializers


from .models import Category, Comment, Post

from django.contrib.auth import get_user_model

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
    categories = CategorySerializer(many=True)
    author = AuthorSerializer(read_only=True)
    # author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'categories', 'author']

    def create(self, validated_data):
        author = validated_data['author']
        return super().create(validated_data)

