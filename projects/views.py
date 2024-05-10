from django.shortcuts import render
from projects.models import Project

def project_index(request):
    template = 'project_index.html'
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, template, context)

def project_detail(request, project_id):
    template = 'project_detail.html'
    project = Project.objects.get(pk=project_id)
    context = {
        'project': project,
    }
    return render(request, template, context)
