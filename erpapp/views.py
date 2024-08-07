from rest_framework import viewsets
from .models import Homework,Teacher,Team,Student,Lesson
from .serializers import  LessonSerializers,TeacherSerializers,HomeworkSerializers
from .permissions import CastomPermission,CoursePermission

class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializers
    permission_classes = [CastomPermission]



class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    permission_classes = [CastomPermission]

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers
    permission_classes = [CastomPermission]
