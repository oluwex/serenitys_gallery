from django.shortcuts import render
from django.views.generic import ListView, DetailView

from gallery.models import Design

# Create your views here.

class ProjectListView(ListView):
    model = Design
    template_name = 'gallery/projects.html'


class ProjectDetailView(DetailView):
    model = Design
    template_name = 'gallery/project_details.html'


def index(request):
    return render(request, 'gallery/index.html')


def about(request):
    return render(request, 'gallery/about.html')


def projects(request):
    return render(request, 'gallery/projects.html')


def project_detail(request):
    return render(request, 'gallery/project_details.html')