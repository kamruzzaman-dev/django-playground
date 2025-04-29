from django.shortcuts import HttpResponse

# Create your views here.
def node_js(request):
    return HttpResponse("Hello from Node.js!")

def home(request):
    return HttpResponse("Node.js homepage!")