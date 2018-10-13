import requests
from django.http import HttpResponse
from django.shortcuts import render
import glob
import os
holder = []
all_html_files = glob.glob("content/*.html")
for single in all_html_files:
    file_name = os.path.basename(single)
    name_only, extension = os.path.splitext(file_name)
    holder.append(name_only)

def homepage(request):
    context = {
        "title": "My Tech Blog", 
        "pages": holder
    }
    return render(request, "homepage.html", context)
    

def bio(request):
    context = {
        "title": "Bio",
        "pages": holder
    }
    return render(request, "bio.html", context)

def contact(request):
    context = {
        "title": "Contact Me",
        "pages": holder
    }
    return render(request, "contact.html", context)

def resume(request):
    context = {
        "title": "Resume",
        "pages": holder
    }
    return render(request, "resume.html", context)

def contact(request):
    response = requests.get('https://api.github.com/users/Jsloopy/repos')
    repos = response.json()
    context = {
        "title": "Contact",
        "pages": holder,
        "github_repos": repos
    }
    
    return render(request, "contact.html", context)


