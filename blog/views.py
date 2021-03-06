from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import BlogSerializer
from .models import Blog, Category


''' class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()   # Если queryset отсутствует, в роутере прописать basename='blog'
    serializer_class = BlogSerializer

    @action(methods=['get'], detail=False)
    def category(self, request):
        categories = Category.objects.all()
        return Response({'categories': [item.title for item in categories]}) '''

# Пагинация для BlogAPIList
class BlogAPIListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class BlogAPIList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = BlogAPIListPagination


class BlogAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticated, )
    #authentication_classes = (TokenAuthentication, )
    

class BlogAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAdminOrReadOnly, )
