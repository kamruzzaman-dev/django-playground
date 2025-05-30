"""
URL configuration for django_playground project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from node_js.views import node_js 
from react_js.views import react_js
from fullstack_development.views import fullstack_development
from backend_development.views import backend_development
from frontend_development.views import frontend_development

urlpatterns = [
    path('admin/', admin.site.urls),
    path('node/', include("node_js.urls")),
    path('react/', include('react_js.urls')),
    path('frontend-development/', include("frontend_development.urls")),
    path('backend-development/', include("backend_development.urls")),
    path('fullstack-development/', include("fullstack_development.urls")),
]
