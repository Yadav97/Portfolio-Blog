from django.shortcuts import render,get_object_or_404

# Create your views here.

from .models import Blog

def allblogs(request):

    blogsfromdb = Blog.objects
    return render(request,"blog/blog.html",{"blogs":blogsfromdb})


def detail(request,blog_id):
    detailblog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':detailblog})   

#this above fnction is use for when localhost:8000/blog/1 or 2 
#here pk = primary key that is our blog_id
#get_object_or_404 is a function either reciev objet or 404 of website