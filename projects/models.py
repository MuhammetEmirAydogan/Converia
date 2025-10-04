# projects/models.py

import uuid
from django.db import models
from users.models import User

class Project(models.Model):
    class DifficultyLevel(models.TextChoices):
        BEGINNER = "beginner", "Başlangıç"
        INTERMEDIATE = "intermediate", "Orta"
        ADVANCED = "advanced", "İleri"

    class ProjectStatus(models.TextChoices):
        PENDING_APPROVAL = "pending_approval", "Onay Bekliyor"
        APPROVED = "approved", "Onaylandı"
        REJECTED = "rejected", "Reddedildi"
        IN_PROGRESS = "in_progress", "Devam Ediyor"
        COMPLETED = "completed", "Tamamlandı"
        CANCELLED = "cancelled", "İptal Edildi"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.JSONField(default=list)
    abstract = models.TextField()
    objectives = models.TextField()
    methodology = models.TextField()
    expected_outcomes = models.TextField()
    
    duration_months = models.PositiveIntegerField(null=True, blank=True)
    difficulty_level = models.CharField(
        max_length=20,
        choices=DifficultyLevel.choices,
        default=DifficultyLevel.INTERMEDIATE
    )
    status = models.CharField(
        max_length=20,
        choices=ProjectStatus.choices,
        default=ProjectStatus.PENDING_APPROVAL
    )
    
    matched_academic = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='matched_projects',
        limit_choices_to={'user_type': User.UserType.ACADEMIC}
    )
    match_score = models.FloatField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    submitted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title