from django.contrib import admin
from .models import User, Course, Student, Teacher, Attendance, Fee, Salary

# Register the User model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role', 'created_at', 'updated_at')
    search_fields = ('name', 'email')  # To allow searching by name or email
    list_filter = ('role',)  # Filter by user role

# Register the Course model
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_description')
    search_fields = ('course_name',)

# Register the Student model
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'grade', 'enrollment_date')
    search_fields = ('user__name',)  # Searching by student's name (through related User)
    list_filter = ('grade',)

# Register the Teacher model
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'salary', 'hire_date')
    search_fields = ('user__name',)  # Searching by teacher's name (through related User)
    list_filter = ('hire_date',)

# Register the Attendance model
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'attendance_date', 'status')
    search_fields = ('student__user__name', 'course__course_name')
    list_filter = ('status', 'course')

# Register the Fee model
@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ('student', 'amount', 'payment_status', 'due_date')
    search_fields = ('student__user__name',)
    list_filter = ('payment_status',)

# Register the Salary model
@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'amount', 'payment_date')
    search_fields = ('teacher__user__name',)
    list_filter = ('payment_date',)
