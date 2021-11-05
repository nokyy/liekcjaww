from rest_framework import permissions, viewsets
from .models import Post
from .serializers import SerializeTHIS

# Create your views here.

# class CreateNewPost(CreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = SerializeTHIS

class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-date')
    serializer_class = SerializeTHIS
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)