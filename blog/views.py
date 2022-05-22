from django.shortcuts import render
from rest_framework import generics
from .serializers import BlogSerializer
from .models import Blog

# Create your views here.


class BlogAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    