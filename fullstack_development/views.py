from django.shortcuts import HttpResponse

# Create your views here.
def fullstack_development(request):
    return HttpResponse("Hello from fullstack development!")

def home(request):
    return HttpResponse("Fullstack development homepage!")