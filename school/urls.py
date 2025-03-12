from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views  # Regular views for things like course listing
from . import api_views  # API views

# Create the router for API endpoints
router = DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'courses', api_views.CourseViewSet)
router.register(r'students', api_views.StudentViewSet)  # Ensure the students endpoint is correctly registered
router.register(r'teachers', api_views.TeacherViewSet)
router.register(r'attendance', api_views.AttendanceViewSet)
router.register(r'fees', api_views.FeeViewSet)
router.register(r'salaries', api_views.SalaryViewSet)

# URL patterns for regular views and API views
urlpatterns = [
    # Regular views, such as course listing
    path('courses/', views.course_list, name='course_list'),
    path('', views.home, name='home'),  # Home page at the root URL (http://127.0.0.1:8000/)
    
    # API views handled by the router
    path('/api/api/', include(router.urls)),  # Include all API routes handled by the router
]
