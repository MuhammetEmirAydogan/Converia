from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Nesneyi sadece oluşturan kullanıcının düzenlemesine veya silmesine izin verir.
    Diğer herkes sadece okuyabilir (GET).
    """
    def has_object_permission(self, request, view, obj):
        # Okuma izinleri (GET, HEAD, OPTIONS) herkese açıktır.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Yazma izinleri (PUT, DELETE) sadece projenin sahibine (student) aittir.
        return obj.student == request.user