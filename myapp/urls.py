from django.contrib import admin
from django.urls import path, re_path, include
from blog.views import *
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

''' router = routers.DefaultRouter()
router.register(r'blog', BlogViewSet) '''

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/v1/blog-auth/', include('rest_framefowk.urls'))  # Авторизация на основе сессий (cookies)
    #path('api/v1/auth/', include('djoser.urls'))               # Авторизация по токенам djoser
    #re_path(r'^auth/', include('djoser.urls.authtoken'))       # Авторизация по токенам djoser
    #path('api/v1/', include(router.urls))                      # http://127.0.0.1:8000/api/v1/blog/
    path('api/v1/blog/', BlogAPIList.as_view()),
    path('api/v1/blog/<int:pk>', BlogAPIUpdate.as_view()),
    path('api/v1/blogdelete/<int:pk>', BlogAPIDestroy.as_view()),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),   # JWT
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refrash'),  # JWT
    path('api/v1/token/verify', TokenVerifyView.as_view(), name='token_verify'),      # JWT
]
