from django.conf import settings
from django.shortcuts import render
from projects.models import Project

def projects(request):
    page_title = "Projects - " + settings.PAGE_INFORMATION['author_name']
    projects = Project.objects.all()

    context = {
        "page_information": settings.PAGE_INFORMATION,
        "page_title": page_title,
        "projects": projects,
    }

    return render(request, "projects.html", context)
