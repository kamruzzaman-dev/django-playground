from django.shortcuts import HttpResponse, render

# Create your views here.
def node_js(request):
    return render(request, "Node/node.html")

def home(request):
    return render(request, "Common/home.html")
