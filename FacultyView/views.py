from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from .models import Student, Attendance
import qrcode
import socket
from StudentView.views import present, all_students
import datetime
from django.views.decorators.csrf import csrf_exempt

 
def qrgenerator():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]

    link = f"http://{ip}:8000/log-attendance"

    # Function to generate and display a QR code
    def generate_qr_code(link):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("FacultyView/static/FacultyView/qrcode.png")

    generate_qr_code(link)


@csrf_exempt
def faculty_view(request):
    if request.method == "POST":
        student_roll = request.POST["student_id"]
        student = Student.objects.get(s_roll=student_roll)
        if student in present:
            present.remove(student)
        return HttpResponseRedirect("/")

    else:
        qrgenerator()
        return render(
            request,
            "FacultyView/FacultyViewIndex.html",
            {
                "students": present,
            },
        )


def add_manually(request):
    date = datetime.datetime.now()
    present_students = Attendance.objects.filter(date=date)
    students = Student.objects.all().order_by("s_roll")
    return render(
        request,
        "StudentView/StudentViewIndex.html",
        {
            "students": students,
            "present_students": present_students,
        },
    )


def print_attendance(req):
    return render(
        req,
        "FacultyView/print.html"
    )


def all_students(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Invalid request method. Use GET.'}, status=400)
    students = Student.objects.all().order_by("s_roll")
    data = []
    for student in students:
        student_dict = {
          's_roll': student.s_roll,
          's_fname': student.s_fname,
          's_lname': student.s_lname,}
        data.append(student_dict)
    return JsonResponse(data, safe=False)


def present_students(request):
    date = datetime.datetime.now()
    if request.method != 'GET':
        return JsonResponse({'error': 'Invalid request method. Use GET.'}, status=400)
    students = Attendance.objects.filter(date=date)
    data = []
    for student in students:
        student_dict = {
          's_roll': student.student.s_roll,
          's_fname': student.student.s_fname,
          's_lname': student.student.s_lname,}
        data.append(student_dict)
    return JsonResponse(data, safe=False)


def log_attendance(req):
    return render(
        req,
        "FacultyView/login.html"
    )