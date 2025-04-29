from django.shortcuts import HttpResponse, render

# Create your views here.
def frontend_development(request):
    return render(request, "frontend-development.html")

def home(request):
    return render(request, "home.html")
