from django.shortcuts import HttpResponse, render

# Create your views here.
def frontend_development(request):
    return render(request, "FE/frontend-development.html")

def home(request):
    name = {'which':"Frontend Development"}
    return render(request, "Common/home.html", context=name)
