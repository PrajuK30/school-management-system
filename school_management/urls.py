"""
URL configuration for school_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# school_management/urls.py
from django.contrib import admin
from django.urls import path, include  # include is required to include app URLs
from school import views  # Import the views from school app (not course_list directly)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('school.urls')),  # This will include all URLs from school/urls.py
    path('courses/', views.course_list, name='course_list'),  # Now this is correct
    path('', views.home, name='home'),  # Set the root URL (/) to the home view

    
    
    

]


# school/views.py
from django.shortcuts import render


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})



