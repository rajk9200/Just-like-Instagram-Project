from django.shortcuts import render
from .models import Posts
# Create your views here.

def show_posts(request):
    post= Posts.objects.all()

    context ={
        'post':post,
    }

    return render(request,'posts/add-posts.html',context)