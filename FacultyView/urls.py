from . import views
from django.urls import path

urlpatterns = [
    path("", views.faculty_view, name="faculty_view"),
    path("add_manually", views.add_manually, name="add_manually"),
    path("all-students", views.all_students, name="all_students_view"), 
    path('present-students', views.present_students),
    path('print-attendance', views.print_attendance),
    path('log-attendance', views.log_attendance)
]
