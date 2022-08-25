from django.http import HttpResponse
from projects.models import Projects
from django.shortcuts import render
from datetime import  datetime
from django.contrib import messages




def home(request):
    project_count = Projects.objects.all().count()
    
    if project_count == 0:
        isempty = True
    else:
        isempty = False

    project = Projects.objects.all()

    context = {
        "project":project,
        "isempty":isempty
	}

    return render(request, 'main/home.html', context)
