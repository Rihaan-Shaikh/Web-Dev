"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.http import HttpResponse
from users.views import SaveResumeView, MyResumesView, CurrentUserView

def home(request):
    return HttpResponse("Django backend running")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/save-resume/', SaveResumeView.as_view(), name='save-resume'),
    path('api/my-resumes/', MyResumesView.as_view(), name='my-resumes'),
    path('api/me/', CurrentUserView.as_view(), name='current-user'),
    path('dashboard/', lambda request: HttpResponse("Dashboard"), name='dashboard'),
    path('', home, name='home'),
]
