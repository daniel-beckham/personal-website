from django.conf import settings
from django.shortcuts import render

def home(request):
    context = {
        "page_information": settings.PAGE_INFORMATION,
    }

    return render(request, "home.html", context)
