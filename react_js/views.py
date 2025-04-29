from django.shortcuts import HttpResponse, render

# Create your views here.
def react_js(request):
    return render(request, "React/react.html")

def home(request):
    return render(request, "Common/home.html")
