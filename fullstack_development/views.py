from django.shortcuts import HttpResponse, render

# Create your views here.
def fullstack_development(request):
    return render(request, "fullstack-development.html")

def home(request):
    return render(request, "home.html")
