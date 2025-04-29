from django.shortcuts import HttpResponse, render

# Create your views here.
def react_js(request):
    course ='React JS and Next.js'
    total_class= 30
    seat= 25
    class_duration= '3 months'
    offering = {
        'course': course,
        'total_class': total_class,
        'seat': seat,
        'class_duration': class_duration
    }
    return render(request, "React/react.html", context=offering)

def home(request):
    name = {'which':"React"}
    return render(request, "Common/home.html", context=name)
