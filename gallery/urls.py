from django.urls import path

from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    # path('projects', views.projects, name='projects'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('projects/project/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('projects/project/', views.project_detail, name='project_detail'),
]