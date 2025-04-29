from django.shortcuts import HttpResponse, render

# Create your views here.
def react_js(request):
    return render(request, "React/react.html")

def home(request):
    name = {'which':"React"}
    return render(request, "Common/home.html", context=name)
