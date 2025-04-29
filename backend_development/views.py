from django.shortcuts import HttpResponse, render

# Create your views here.
def backend_development(request):
    return render(request, "backend-development.html")

def home(request):
    return render(request, "home.html")
