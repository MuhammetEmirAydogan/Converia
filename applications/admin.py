# applications/admin.py

from django.contrib import admin
from .models import ProjectApplication

class ProjectApplicationAdmin(admin.ModelAdmin):
    list_display = ('project', 'get_student', 'academic', 'status', 'created_at')
    list_filter = ('status', 'academic')
    search_fields = ('project__title', 'academic__username', 'project__student__username')
    readonly_fields = ('created_at', 'updated_at', 'responded_at')

    # admin panelinde project objesinden student'ın username'ini almak için
    @admin.display(description='Öğrenci')
    def get_student(self, obj):
        return obj.project.student.username

admin.site.register(ProjectApplication, ProjectApplicationAdmin)