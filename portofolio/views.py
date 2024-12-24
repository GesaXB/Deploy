from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Skill, Project

def base(request):
    message = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            message = "There was an error. Please check the form."
    else:
        form = ContactForm()

    return render(request, 'portofolio/base.html', {
        'skills': Skill.objects.all(),
        'projects': Project.objects.all(),
        'form': form,
        'message': message,
    })

def portfolio(request):
    return render(request, 'portfolio.html', {'projects': Project.objects.all()})

def skills_view(request):
    return render(request, 'skils.html', {'skills': Skill.objects.all()})

def contact_view(request):
    return render(request, 'contact.html', {'form': ContactForm(request.POST) if request.method == 'POST' else ContactForm()})
