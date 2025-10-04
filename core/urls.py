# core/urls.py dosyasının son hali

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # App URL'leri
    path("api/users/", include("users.urls")),
    path("api/projects/", include("projects.urls")), # <-- YENİ EKLENEN SATIR

    # JWT Token URL'leri
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]