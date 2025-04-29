from django.shortcuts import HttpResponse

# Create your views here.
def react_js(request):
    return HttpResponse("Hello from React.js!")

def home(request):
    return HttpResponse("React.js homepage!")