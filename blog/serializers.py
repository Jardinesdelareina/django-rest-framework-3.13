from rest_framework import serializers


class BlogSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    text = serializers.CharField(max_length=2000)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    category = serializers.CharField()
