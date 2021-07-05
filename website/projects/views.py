from django.shortcuts import render
from projects.models import Project

def projects(request):
    projects = Project.objects.all()
    context = { "projects": projects }
    return render(request, "projects.html", context)
