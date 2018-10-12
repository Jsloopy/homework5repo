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
    # content_html = open("content/homepage.html").read()
    context = {
        "title": "My Tech Blog", 
        "pages": holder
    }
    return render(request, "homepage.html", context)
    

def bio(request):
    # content_html = open("content/bio.html").read() 
    context = {
        # "content": content_html,
        "title": "Bio",
        "pages": holder
    }
    return render(request, "bio.html", context)

def contact(request):
    # content_html = open("content/contact.html").read() 
    context = {
        # "content": content_html, 
        "title": "Contact Me",
        "pages": holder
    }
    return render(request, "contact.html", context)

def resume(request):
    # content_html = open("content/resume.html").read() 
    context = {
        # "content": content_html, 
        "title": "Resume",
        "pages":holder
    }
    return render(request, "resume.html", context)


# Create your views here.
