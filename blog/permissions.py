from rest_framework import permissions

# Кастомные ограничения доступа

# AllowAny - полный доступ
# IsAuthentificated - только для авторизованных пользователей
# IsAdminUser - только для администраторов
# IsAuthenticatedOrReadOnly - только для авторизованных, или всем, но для чтения

# Для админа или только для чтения
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
            

# Для автора или только для чтения
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user