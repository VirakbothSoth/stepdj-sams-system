from django import forms
from .models import Subject, Classroom, Student, Teacher, Attendance
import datetime

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'category']

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['class_code', 'name', 'subject']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'age', 'classroom']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'email', 'age', 'salary', 'classroom']

class AttendanceForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=datetime.date.today
    )
    class Meta:
        model = Attendance
        fields = ['classroom', 'date']