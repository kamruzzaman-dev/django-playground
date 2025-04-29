from django.shortcuts import HttpResponse, render

# Create your views here.
def fullstack_development(request):
    return render(request, "FS/fullstack-development.html")

def home(request):
    name = {'which':"Fullstack Development"}
    return render(request, "Common/home.html", context=name)