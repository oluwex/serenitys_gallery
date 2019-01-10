from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView

from .forms import MessageForm
from .models import Design, Message


# Create your views here.

class ProjectListView(ListView):
    model = Design
    template_name = 'gallery/projects.html'
    paginate_by = 10


class ProjectDetailView(DetailView):
    model = Design
    template_name = 'gallery/project_details.html'


class ContactView(SuccessMessageMixin, CreateView):
    model = Message
    template_name = 'gallery/contact.html'
    form_class = MessageForm
    success_url = '/contact/'
    success_message = "Message successfully sent"

    def form_valid(self, form):
        form.instance.sender_ip = self.request.META['REMOTE_ADDR']
        return super(ContactView, self).form_valid(form)


def index(request):
    recent_designs = Design.objects.all()[:6]
    context = {
        'designs': recent_designs,
    }
    return render(request, 'gallery/index.html', context)


def about(request):
    return render(request, 'gallery/about.html')


def projects(request):
    return render(request, 'gallery/projects.html')


def project_detail(request):
    return render(request, 'gallery/project_details.html')


def contact(request):
    return render(request, 'gallery/contact.html')