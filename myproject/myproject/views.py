from django.http import HttpResponse


def index(request):
    return HttpResponse("hello world")

def home(request):
    return HttpResponse("<h1 style='color:red'>Hello welcome to my home</h1>")


#localhost/simran/12 (localhost/name/age) 
#if age<18 --> name cannot vote
#if age>=18 --> name can vote
#myproject --> urls (path)
              #views (function)
#blogproject --> users ---> urls,views,admin....