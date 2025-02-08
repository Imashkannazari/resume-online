from django.shortcuts import render
from .models import Profile, Experience, Education, Skill, Project

def resume_view(request):
    profile = Profile.objects.first()
    experience = Experience.objects.filter(profile=profile)
    education = Education.objects.filter(profile=profile)
    skill = Skill.objects.filter(profile=profile)
    projects = Project.objects.filter(profile=profile)
    
    context = {
        'profile': profile,
        'experience': experience,
        'education': education,
        'skill': skill,
        'projects': projects
    }
    return render(request, 'resume.html', context)