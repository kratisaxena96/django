from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login  #import Login class from forms file in pwd 
# Create your views here.

def index(request):
    #return HttpResponse("Welcome to my users app")
    return render(request,"index.html")

def home(request):
    return HttpResponse("THIS IS MY HOME OF DJANGO")

def login(request):
    form = Login()
    return render(request,"login.html",{'form':form})



#myproject
#manage.py
#blog
#users --> templates
#templates (html pages)
#static (css,images)