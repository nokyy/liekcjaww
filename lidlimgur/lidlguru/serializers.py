from rest_framework import serializers
from .models import Post

class SerializeTHIS(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'categories']

    def update(self, request, instance):
        instance.author = request.user