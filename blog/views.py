from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogSerializer
from .models import Blog

# Create your views here.

class BlogAPIList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogAPIUpdate(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogAPIDetaivView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

''' class BlogAPIView(APIView):


    def get(self, request):
        blog = Blog.objects.all()
        return Response({'notes': BlogSerializer(blog, many=True).data})


    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'note': serializer.data})


    def put(self, request, *agrs, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})
        try:
            instance = Blog.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists'})
        
        serializer = BlogSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'note': serializer.data})
 '''