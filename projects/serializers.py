from rest_framework import serializers
from .models import Project
from users.serializers import UserProfileSerializer

class ProjectSerializer(serializers.ModelSerializer):

    student = UserProfileSerializer(read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'student', 'title', 'description', 'keywords', 
            'abstract', 'objectives', 'methodology', 'expected_outcomes',
            'duration_months', 'difficulty_level', 'status', 'created_at'
        ]
        
        read_only_fields = ['status', 'student']

    def create(self, validated_data):
      
        student = self.context['request'].user
        project = Project.objects.create(student=student, **validated_data)
        return project