from django.shortcuts import render
from .models import Skill, Project

def base(request):
    if request.method == 'POST':
        name, email, message = (request.POST['name'], request.POST['email'], request.POST['message'])
    return render(request, 'portofolio/base.html', {
        'skills': Skill.objects.all(),
        'projects': Project.objects.all()
    })

def portfolio(request):
    return render(request, 'portfolio.html', {'projects': Project.objects.all()})

def skills_view(request):
    return render(request, 'skils.html', {'skills': Skill.objects.all()})
