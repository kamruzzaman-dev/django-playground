from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('fullstack-development/', views.fullstack_development),
]
