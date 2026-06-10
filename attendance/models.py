from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.category}"


class Classroom(models.Model):
    class_code = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.class_code}"


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.classroom.name}"


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.classroom.name}"


class Attendance(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['classroom', 'date']

    def __str__(self):
        return f"{self.classroom.name} - {self.date}"


class AttendanceDetail(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('permission', 'Permission'),
    ]
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='present')

    def __str__(self):
        return f"{self.student.name} - {self.status}"