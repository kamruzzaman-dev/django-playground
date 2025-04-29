from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('node-js/', views.node_js),
]
