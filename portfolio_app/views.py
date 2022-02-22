from django.http import HttpResponse
from django.shortcuts import render
from . models import Project
from blog.models import Blog
# Create your views here.

def home(request):
    projects = Project.objects.all().order_by("-created")
    projects = projects[:3]

    blogs = Blog.objects.all().order_by("-created")
    blogs = blogs[:3]
    context = {'projects': projects, 'blogs':blogs}
    return render(request, 'portfolio_app/home.html', context)

def projects(request):
    projects = Project.objects.all()
    projects = projects.order_by("-created")

    blogs = Blog.objects.all()
    blogs = blogs.order_by("-created")

    context = {'projects': projects, 'blogs':blogs}
    return render(request, 'portfolio_app/projects.html', context)

def singleProject(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project': project}
    return render(request, 'portfolio_app/single-project.html', context)