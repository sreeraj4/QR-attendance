from django.shortcuts import render
from FacultyView.models import Student, Attendance
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
import datetime
import json

# Create your views here.
all_students = set()
present = set()


def add_manually_post(request):
    student_roll = request.POST["student-name"]
    student = Student.objects.get(s_roll=student_roll)
    present.add(student)
    return HttpResponseRedirect("/submitted")
    

def all_students(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Invalid request method. Use GET.'}, status=400)
    

# listent o post reqests
@csrf_exempt
def req_mark_attendance(request):
    date = datetime.datetime.now()
    if request.method != 'POST':
        return JsonResponse({'message': 'Invalid request method. Use POST.'}, status=400)
    try:
        data = json.loads(request.body)
        student_roll = data.get('student-name')
        student = Student.objects.get(s_roll=student_roll)
    except KeyError:
        return JsonResponse({'message': 'Missing student name in request.'}, status=400)
    except ObjectDoesNotExist:
        return JsonResponse({'message': 'Student with roll number not found.'}, status=404)
    try:
        attendance, created = Attendance.objects.get_or_create(student=student, date=date, defaults={'attendance': True})
        if created:
            return JsonResponse({'message': 'Student marked as Present', 'action': 'add'})
        else:
            attendance.delete()
            return JsonResponse({'message': 'Student marked as absent', 'action': 'remove'})
    except Attendance.DoesNotExist:
        pass


def submitted(request):
    return render(request, "StudentView/Submitted.html")
