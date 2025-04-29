from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('react-js/', views.react_js),
]
