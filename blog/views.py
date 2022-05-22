from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogSerializer
from .models import Blog

# Create your views here.


class BlogAPIView(APIView):
    def get(self, request):
        blog = Blog.objects.all()
        return Response({'notes': BlogSerializer(blog, many=True).data})

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        note_new = Blog.objects.create(
            title=request.data['title'],
            text=request.data['text'],
            category=request.data['category']
        )

        return Response({'note': BlogSerializer(note_new).data})
    