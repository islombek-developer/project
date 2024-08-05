from django.db import models
from django.contrib.auth.models import User




class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    date_of = models.DateField(null=True,blank=True )

    def __str__(self):
        return self.user.username

    

class Team(models.Model):
    name=models.CharField(max_length=70, unique=True)
    date_created=models.DateField(auto_now_add=True)
    end_date=models.DateField(blank=True, null=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='teacher',null=True,blank=True)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    date_of_birth=models.DateField(blank=True, null=True)
    team=models.ForeignKey(Team, on_delete=models.CASCADE, related_name='students',null=True,blank=True)

    def __str__(self):
        return self.user.first_name
    
class Lesson(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='lesson')
    title = models.CharField(max_length=100, unique=True)
    date = models.DateField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    homework_status = models.BooleanField(default=False)


    class Meta:
        unique_together = ['team', 'title']

    def __str__(self):
        return self.title


class Homework(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, related_name='homework')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, related_name='homeworks')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='students')
    description = models.TextField()
    homework_file = models.FileField(upload_to='homeworks', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['student', 'team']

    def __str__(self):
        return f"{self.student.user.first_name}-- {self.lesson.title}"