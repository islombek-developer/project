from rest_framework import serializers
from .models import Teacher,Team,Student,Homework,Lesson

class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class HomeworkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'


class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'