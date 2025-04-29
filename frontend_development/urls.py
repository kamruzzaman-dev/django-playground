from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('frontend-development/', views.frontend_development),
]
