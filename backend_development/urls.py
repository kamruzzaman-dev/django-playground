from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('backend-development/', views.backend_development),
]
