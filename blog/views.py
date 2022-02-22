from django.shortcuts import render
from . models import Blog
# Create your views here.

def blogs(request):
    blogs = Blog.objects.all().order_by("-created")
    num = len(blogs)
    context = {'blogs': blogs, 'num': num}

    return render(request, 'blog/blogs.html', context)

def singlePost(request, pk):
    blog = Blog.objects.get(id=pk)
    context = {'blog': blog}
    return render(request, 'blog/single-post.html', context)