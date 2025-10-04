from rest_framework import serializers
from .models import User, StudentProfile, AcademicProfile

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'user_type']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            user_type=validated_data.get('user_type', User.UserType.STUDENT)
        )

        if user.user_type == User.UserType.STUDENT:
            StudentProfile.objects.create(user=user)
        elif user.user_type == User.UserType.ACADEMIC:
            AcademicProfile.objects.create(user=user)
        
        return user

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['student_number', 'department', 'grade', 'gpa', 'cv_file', 'interests']

class AcademicProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicProfile
        fields = ['title', 'department', 'expertise_areas', 'research_interests', 'max_students', 'cv_file']

class UserProfileSerializer(serializers.ModelSerializer):
    student_profile = StudentProfileSerializer(read_only=True)
    academic_profile = AcademicProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'user_type', 'student_profile', 'academic_profile'
        ]