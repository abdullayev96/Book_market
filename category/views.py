from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User


def index(request):
    books  = Book.objects.all().order_by('id')

    ctx  = {
        "books":books
    }


    return render(request, 'index.html', ctx)


def Blog_page(request):
    blogs = Blog.objects.all()

    ctx = {
        "blogs":blogs
    }
    return render(request, 'blog.html', ctx)


def Blog_detail(request, pk):
    blog = Blog.objects.get(id=pk)

    ctx = {
        'blog':blog
    }

    return render(request, 'blog_detail.html', ctx)



