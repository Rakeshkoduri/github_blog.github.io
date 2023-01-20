from django.shortcuts import render
from .models import BlogModel
from .forms import *


def home(request):
    context = {}
    return render(request, 'blog/home.html', context)


def contact(request):
    return render(request,'blog/contact.html')

def about(request):
    return render(request,'blog/about.html')


def blog_list(request):
    blogs = BlogModel.objects.all().order_by('-created')
    context = {
        'blogs': blogs
    }
    return render(request,'blog/blog_list.html',context)


def blog_detail(request,pk):
    blog = BlogModel.objects.get(pk=pk)
    context = {
        'blog': blog
    }
    return render(request, 'blog/blog_detail.html', context)
