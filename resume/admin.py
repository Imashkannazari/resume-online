from django.contrib import admin
from .models import Profile, Skill, Experience, Project, Education

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Education)