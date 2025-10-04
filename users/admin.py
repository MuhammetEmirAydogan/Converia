# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, StudentProfile, AcademicProfile

# Bizim custom User modelimizi, Django'nun gelişmiş UserAdmin arayüzü ile
# admin paneline kaydediyoruz. Bu sayede şifre değiştirme, yetki atama gibi
# özellikler hazır olarak gelir.
class CustomUserAdmin(UserAdmin):
    model = User
    # Admin panelinde kullanıcı listesinde gösterilecek alanlar
    list_display = ['username', 'email', 'user_type', 'first_name', 'last_name', 'is_staff']
    # Kullanıcı düzenleme sayfasında alanları gruplama
    fieldsets = UserAdmin.fieldsets + (
        ('Ek Bilgiler', {'fields': ('user_type', 'phone_number', 'is_verified')}),
    )

# Modellerimizi admin paneline kaydediyoruz.
admin.site.register(User, CustomUserAdmin)
admin.site.register(StudentProfile)
admin.site.register(AcademicProfile)