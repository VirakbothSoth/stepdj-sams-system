from django.views.generic import RedirectView
from django.urls import path
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/dashboard/'), name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/<int:pk>/edit/', views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),

    path('classes/', views.classroom_list, name='classroom_list'),
    path('classes/create/', views.classroom_create, name='classroom_create'),

    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/create/', views.subject_create, name='subject_create'),

    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/create/', views.teacher_create, name='teacher_create'),

    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/create/', views.attendance_create, name='attendance_create'),
    path('attendance/<int:pk>/', views.attendance_detail, name='attendance_detail'),
    path('attendance/<int:pk>/mark/', views.attendance_mark, name='attendance_mark'),
]