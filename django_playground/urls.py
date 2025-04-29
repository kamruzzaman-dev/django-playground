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
from django.urls import path
from node_js import views as node_js_view
from react_js import views as react_js_view
from fullstack_development import views as fullstack_development_view
from backend_development import views as backend_development_view
from frontend_development import views as frontend_development_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('node/', node_js_view.home),
    path('node/node-js', node_js_view.node_js),
    path('react/', react_js_view.home),
    path('react/react-js', react_js_view.react_js),
    path('frontend-development/', frontend_development_view.home),
    path('frontend-development/frontend-development', frontend_development_view.frontend_development),
    path('backend-development/', backend_development_view.home),
    path('backend-development/backend-development', backend_development_view.backend_development),
    path('fullstack-development/', frontend_development_view.home),
    path('fullstack-development/fullstack-development', fullstack_development_view.fullstack_development),
]
