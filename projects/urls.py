"""project_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    ProjectListView,
    ProjectDetailView, 
    ProjectDeleteView, 
    ProjectUpdateView, 
    TaskDeleteView, 
    TaskDetailView,
    TaskUpdateView,
)
from . import views

app_name = 'projects'

urlpatterns = [
    path('dashboard/', ProjectListView.as_view(), name='dashboard'),
    path('new/project/', views.form, name='new-project'),
    path('<pk>/project/new/task/', views.task_form, name='new-task'),
    path('<pk>/project/unfinished/', views.project_incomplete, name='project-incomplete'),
    path('<pk>/project/completed/', views.project_complete, name='project-complete'),
    path('<pk>/task/unfinished/', views.task_incomplete, name='task-incomplete'),
    path('<pk>/task/completed/', views.task_complete, name='task-complete'),
    path('<pk>/project/update/', ProjectUpdateView.as_view(), name='update-project'),
    path('<pk>/project/task/update/', TaskUpdateView.as_view(), name='update-task'),
    path('<pk>/project/delete/', ProjectDeleteView.as_view(), name='delete-project'),
    path('<pk>/project/task/delete/', TaskDeleteView.as_view(), name='delete-task'),
    path('<pk>/project/',ProjectDetailView.as_view(), name='project-detail-view'),
    path('<pk>/task/',TaskDetailView.as_view(), name='task-detail-view'),
    path('', ProjectListView.as_view(), name='home-view')
]