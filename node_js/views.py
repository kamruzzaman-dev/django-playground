from django.shortcuts import HttpResponse, render

# Create your views here.
def node_js(request):
    return render(request, "node.html")

def home(request):
    return render(request, "home.html")
