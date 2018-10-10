import requests
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    content_html = open("content/homepage.html") 
    context = {
        "content": content_html, 
    }
    return render(request, "base.html", context)
    

def bio(request):
    content_html = open("content/bio.html") 
    context = {
        "content": content_html, 
    }
    return render(request, "base.html", context)

def contact(request):
    content_html = open("content/contact.html") 
    context = {
        "content": content_html, 
    }
    return render(request, "base.html", context)

def resume(request):
    content_html = open("content/resume.html") 
    context = {
        "content": content_html, 
    }
    return render(request, "base.html", context)


# Create your views here.
