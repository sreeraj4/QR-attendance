from django.contrib import admin

# Register your models here.

from .models import Student, Attendance, Section, Year, Branch

admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Section)
admin.site.register(Year)
admin.site.register(Branch)

