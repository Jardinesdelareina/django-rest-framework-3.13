from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import BlogSerializer
from .models import Blog, Category


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()   # Если queryset отсутствует, в роутере прописать basename='blog'
    serializer_class = BlogSerializer

    @action(methods=['get'], detail=False)
    def category(self, request):
        categories = Category.objects.all()
        return Response({'categories': [item.title for item in categories]})
