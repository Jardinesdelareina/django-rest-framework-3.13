from rest_framework import serializers
from .models import *


class BlogSerializer(serializers.ModelSerializer):
    # Создается скрытое поле и по умолчанию заполняется текущим авторизованным юзером
    # Связывается с атрибутом user из модели Blog
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Blog
        fields = '__all__'
