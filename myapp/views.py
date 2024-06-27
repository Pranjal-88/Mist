from django.shortcuts import render
from .models import Post


def index(request):
    collection=Post.objects.all()
    return render(request,"index.html",{'collections':collection})

def post(request,post_id):
    current_post=Post.objects.get(id=post_id)
    return render(request,"post.html",{'post':current_post})

def contact(request):
    return render(request,"contact.html")
