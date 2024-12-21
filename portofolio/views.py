from django.shortcuts import render
from .models import Skill, Project

# Halaman Utama (Landing Page)
def base(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    
    # Cek apakah form kontak dikirim
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        # Simpan pesan kontak (bisa menggunakan model ContactMessage)
        # Contoh: ContactMessage.objects.create(name=name, email=email, message=message)
        
    return render(request, 'portofolio/base.html', {'skills': skills, 'projects': projects})


def skills_view(request):
    skills = Skill.objects.all()  # Ambil semua data dari model Skill
    return render(request, 'skils.html', {'skills': skills})

