# applications/models.py

import uuid
from django.db import models
from users.models import User
from projects.models import Project

class ProjectApplication(models.Model):
    class ApplicationStatus(models.TextChoices):
        PENDING = "pending", "Beklemede"
        ACCEPTED = "accepted", "Kabul Edildi"
        REJECTED = "rejected", "Reddedildi"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='applications')
    academic = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='applications_received',
        limit_choices_to={'user_type': User.UserType.ACADEMIC}
    )
    status = models.CharField(
        max_length=20,
        choices=ApplicationStatus.choices,
        default=ApplicationStatus.PENDING
    )
    message = models.TextField(blank=True) # Öğrencinin akademisyene notu
    academic_response = models.TextField(blank=True) # Akademisyenin öğrenciye yanıtı
    match_score = models.FloatField(null=True, blank=True) # Eşleşme algoritmasından gelen skor

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    responded_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        # Bir öğrenci, bir projeyle bir akademisyene sadece bir kere başvurabilir.
        unique_together = ('project', 'academic')

    def __str__(self):
        return f"Başvuru: {self.project.title} -> {self.academic.username}"