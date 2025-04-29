from django.shortcuts import HttpResponse

# Create your views here.
def frontend_development(request):
    return HttpResponse("Hello from frontend development!")

def home(request):
    return HttpResponse("Frontend development homepage!")