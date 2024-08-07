from django.contrib import admin
from .models import Teacher,Team,Student,Lesson,Homework



admin.site.register(Team)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Homework)
admin.site.register(Lesson)