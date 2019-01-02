from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'gallery/index.html')


def about(request):
    return render(request, 'gallery/about.html')


def projects(request):
    return render(request, 'gallery/projects.html')