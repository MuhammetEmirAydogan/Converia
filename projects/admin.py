# projects/admin.py

from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'student', 'status', 'difficulty_level', 'created_at')
    list_filter = ('status', 'difficulty_level', 'student__academicprofile__department')
    search_fields = ('title', 'description', 'student__username')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Project, ProjectAdmin)