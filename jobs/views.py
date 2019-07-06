from django.shortcuts import render

# Create your views here.

from .models import Jobs

def home(request):
    jobsfromdb = Jobs.objects

    return render(request,"jobs/home.html",{"jobs":jobsfromdb})