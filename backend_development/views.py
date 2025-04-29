from django.shortcuts import HttpResponse

# Create your views here.
def backend_development(request):
    return HttpResponse("Hello from backend development!")

def home(request):
    return HttpResponse("Backend development homepage!")