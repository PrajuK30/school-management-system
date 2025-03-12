from rest_framework import viewsets
import os
from django.conf import settings

from .models import User, Course, Student, Teacher, Attendance, Fee, Salary
from .serializers import UserSerializer, CourseSerializer, StudentSerializer, TeacherSerializer, AttendanceSerializer, FeeSerializer, SalarySerializer
from django.shortcuts import render
from .models import Course  # Import the Course model

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class FeeViewSet(viewsets.ModelViewSet):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer

class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer


# school/views.py

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'school/course_list.html', {'courses': courses})

def home(request):
    courses = Course.objects.all()  # Fetch the courses in the home view
    return render(request, 'school/home.html', {'courses': courses}) 
