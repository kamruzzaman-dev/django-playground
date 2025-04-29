from django.shortcuts import HttpResponse, render

# Create your views here.
def react_js(request):
    return render(request, "react.html")

def home(request):
    return render(request, "home.html")
