from rest_framework import generics, viewsets
from .serializers import BlogSerializer
from .models import Blog


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
