from rest_framework import generics, permissions
from .models import Project
from .serializers import ProjectSerializer
from .permissions import IsOwnerOrReadOnly

class ProjectListCreateView(generics.ListCreateAPIView):
    """
    Projeleri listeler veya yeni bir proje oluşturur.
    Sadece giriş yapmış kullanıcılar erişebilir.
    """
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Tek bir projeyi görüntüler, günceller veya siler.
    Sadece projenin sahibi düzenleme veya silme yapabilir.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]