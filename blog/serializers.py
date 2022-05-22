from dataclasses import field
from rest_framework import serializers
from .views import *
from .models import *


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


''' class BlogSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    text = serializers.CharField(max_length=2000)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    category = serializers.CharField()


    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
 '''