from django.contrib import admin
from .models import Skill, Project, ContactMessage, CV

# Skill Admin
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# Project Admin
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'get_skills', 'github_link', 'demo_link')
    search_fields = ('title', 'description')
    filter_horizontal = ('skills',)  # Menggunakan 'skills'
    list_filter = ('skills__name',)  # Filter berdasarkan nama skill

    # Menampilkan daftar skill dalam proyek
    def get_skills(self, obj):
        return ", ".join([skill.name for skill in obj.skills.all()])
    get_skills.short_description = 'Skills'

# ContactMessage Admin
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)

# CV Admin
@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')
    search_fields = ('file',)
    list_filter = ('uploaded_at',)
