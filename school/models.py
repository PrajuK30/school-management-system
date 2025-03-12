from django.db import models

# User model for managing different roles
class User(models.Model):
    ADMIN = 'admin'
    TEACHER = 'teacher'
    STUDENT = 'student'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student')
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Course model for course management
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()

    def __str__(self):
        return self.course_name
    
    
    


# Student model related to user
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.CharField(max_length=50)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name

# Teacher model related to user and salary
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()


    def __str__(self):
        return self.user.name

# Attendance model to track student attendance
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    attendance_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent'), ('late', 'Late')])

    def __str__(self):
        return f'{self.student.user.name} - {self.course.course_name}'

# Fee model for managing student fees
class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=10, choices=[('paid', 'Paid'), ('pending', 'Pending')])
    due_date = models.DateTimeField()

    def __str__(self):
        return f'{self.student.user.name} - {self.amount}'

# Salary model for managing teacher salaries

class Salary(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name='salary_record')  # Add related_name here
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()



    def __str__(self):
        return f'{self.teacher.user.name} - {self.amount}'
    
    
    

  
    


  

    
    
  