from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/bloglist/', BlogAPIList.as_view()),
    path('api/v1/bloglist/<int:pk>', BlogAPIUpdate.as_view()),
    path('api/v1/blogdetail/<int:pk>', BlogAPIDetaivView.as_view()),
]
