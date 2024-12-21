from django.db import models

# Skill Model
class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='skills/', blank=True)

    def __str__(self):
        return self.name

# Project Model
class Project(models.Model):
    title = models.CharField(max_length=200)
    skills = models.ManyToManyField(Skill, related_name='projects')  # Ganti 'category' jadi 'skills'
    description = models.TextField()
    tech_stack = models.TextField()  # Teknologi yang digunakan
    image = models.ImageField(upload_to='projects/', blank=True)
    github_link = models.URLField(blank=True)
    demo_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

# ContactMessage Model
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

# CV Model
class CV(models.Model):
    file = models.FileField(upload_to='cv/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "CV File"
