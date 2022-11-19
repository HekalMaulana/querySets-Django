from django.shortcuts import render

from .models import post

# Create your views here.
def index (request):
    posts = post.objects.all();
    print (posts)
    context = {
        'title':'Blog | Hekal',
        'subtitle':'Welcome To My Blog',
        'post':posts,
    }

    return render(request,'blog/index.html',context)

def blog (request):
    posts = post.objects.filter(category='blog');
    print (posts)
    context = {
            'title':'Blog | Hekal',
            'subtitle':'Welcome To My Blog For Blog Category',
            'post':posts,
        }

    return render(request,'blog/index.html',context)

def news (request):
    posts = post.objects.filter(category='news');
    print (posts)
    context = {
            'title':'Blog | Hekal',
            'subtitle':'Welcome To My Blog For News Category',
            'post':posts,
        }

    return render(request,'blog/index.html',context)