from django.shortcuts import render
from projects.models import Project

def projects(request):
    page_title = "Projects"
    projects = Project.objects.all()
    context = { "page_title": page_title, "projects": projects }
    return render(request, "projects.html", context)
