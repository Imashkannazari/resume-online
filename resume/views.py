from django.shortcuts import render
from .models import Profile, Experience, Education, Skill, Project

#home view
def home_view(request):
    return render(request, 'home.html')

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

