from django.shortcuts import render
from .models import Category,post

# Create your views here.
def index(request):
    posts=post.objects.all()
    print(posts)
    data = {
        'posts':posts
    }

    return render(request,"index.html",data)



def posts(request, url):
    po = post.objects.get(url=url) 
    #print(po)
    return render(request,'posts.html',{'post':po})


    #return render(request,"posts.html")
