# users/models.py

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Django'nun standart User modelini genişletiyoruz.
    # AbstractUser; username, first_name, last_name, email, password gibi alanları hazır getirir.

    class UserType(models.TextChoices):
        # Kullanıcı tipleri için seçenekler oluşturuyoruz.
        STUDENT = "student", "Öğrenci"
        ACADEMIC = "academic", "Akademisyen"
        ADMIN = "admin", "Admin"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.CharField(
        max_length=10,
        choices=UserType.choices,
        default=UserType.STUDENT
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    # created_at ve updated_at alanları Django'nun kendi User modelinde (dolaylı olarak) mevcuttur.
    # is_active alanı da AbstractUser'dan gelmektedir.

    def __str__(self):
        return self.username


class StudentProfile(models.Model):
    # Her bir Student kullanıcısına bağlı olacak profil modeli.
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    student_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    grade = models.CharField(max_length=20)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    cv_file = models.FileField(upload_to='cvs/students/', null=True, blank=True)
    interests = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - Öğrenci Profili"


class AcademicProfile(models.Model):
    # Her bir Academic kullanıcısına bağlı olacak profil modeli.
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField(max_length=50) # Prof. Dr., Doç. Dr. vs.
    department = models.CharField(max_length=100)
    expertise_areas = models.JSONField(default=list) # ["Yapay Zeka", "Veri Madenciliği"]
    research_interests = models.TextField(blank=True)
    max_students = models.PositiveIntegerField(default=5)
    current_students = models.PositiveIntegerField(default=0)
    cv_file = models.FileField(upload_to='cvs/academics/', null=True, blank=True)
    publications = models.JSONField(default=list, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} {self.user.first_name} {self.user.last_name} - Akademisyen Profili"