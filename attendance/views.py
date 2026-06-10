from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Teacher, Classroom, Subject, Attendance, AttendanceDetail
from .forms import StudentForm, TeacherForm, ClassroomForm, SubjectForm, AttendanceForm
from django.utils import timezone

def dashboard(request):
    today = timezone.now().date()
    today_attendance = Attendance.objects.filter(date=today)
    today_present = AttendanceDetail.objects.filter(attendance__date=today, status='present').count()
    today_absent = AttendanceDetail.objects.filter(attendance__date=today, status='absent').count()
    today_late = AttendanceDetail.objects.filter(attendance__date=today, status='late').count()

    context = {
        'student_count': Student.objects.count(),
        'teacher_count': Teacher.objects.count(),
        'classroom_count': Classroom.objects.count(),
        'subject_count': Subject.objects.count(),
        'attendance_count': Attendance.objects.count(),
        'today_sessions': today_attendance.count(),
        'today_present': today_present,
        'today_absent': today_absent,
        'today_late': today_late,
    }
    return render(request, 'attendance/dashboard.html', context)

def student_list(request):
    students = Student.objects.all()
    return render(request, 'attendance/student_list.html', {'students': students})

def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'attendance/student_form.html', {'form': form})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'attendance/student_detail.html', {'student': student})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'attendance/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'attendance/confirm_delete.html', {'object': student})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'attendance/teacher_list.html', {'teachers': teachers})

def teacher_create(request):
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('teacher_list')
    return render(request, 'attendance/teacher_form.html', {'form': form})

def classroom_list(request):
    classrooms = Classroom.objects.all()
    return render(request, 'attendance/classroom_list.html', {'classrooms': classrooms})

def classroom_create(request):
    form = ClassroomForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('classroom_list')
    return render(request, 'attendance/classroom_form.html', {'form': form})

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'attendance/subject_list.html', {'subjects': subjects})

def subject_create(request):
    form = SubjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('subject_list')
    return render(request, 'attendance/subject_form.html', {'form': form})

def attendance_list(request):
    attendances = Attendance.objects.all()
    return render(request, 'attendance/attendance_list.html', {'attendances': attendances})

def attendance_create(request):
    form = AttendanceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('attendance_list')
    return render(request, 'attendance/attendance_form.html', {'form': form})

def attendance_detail(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    details = AttendanceDetail.objects.filter(attendance=attendance)
    return render(request, 'attendance/attendance_detail.html', {
        'attendance': attendance,
        'details': details
    })

def attendance_history(request, classroom_id):
    classroom = get_object_or_404(Classroom, pk=classroom_id)
    attendances = Attendance.objects.filter(classroom=classroom).order_by('-date')
    return render(request, 'attendance/attendance_history.html',
        {
            'classroom': classroom,
            'attendances': attendances
        }
    )

def attendance_mark(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    students = Student.objects.filter(classroom=attendance.classroom)

    if request.method == 'POST':
        for student in students:
            status = request.POST.get(f'status_{student.id}', 'absent')

            AttendanceDetail.objects.update_or_create(
                attendance=attendance,
                student=student,
                defaults={'status': status}
            )

        return redirect('attendance_list')

    return render(request, 'attendance/attendance_mark.html', {
        'attendance': attendance,
        'students': students,
        'status_choices': AttendanceDetail.STATUS_CHOICES,
    })