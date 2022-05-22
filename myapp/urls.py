from django.contrib import admin
from django.urls import path, include
from blog.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'blog', BlogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))   # http://127.0.0.1:8000/api/v1/blog/
]
