from django.db import models
from django.contrib.auth.models import User


department_choice = [('MATHS','Maths',),
                     ('PHYSICS','Physics'),
                     ('CHEMISTRY','Chemistry')]

present_choice = [('PRESENT','Present'),
                  ('ABSENT','Absent')]


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    department = models.CharField(max_length=10, choices=department_choice,default='')

    def __str__(self):
        return str(self.id) + " "+" " + self.name + " "

class Attendane(models.Model):
    teacher_id = models.IntegerField()
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    is_present = models.CharField(max_length=10, choices=present_choice,default='')

    def __str__(self) -> str:
        return str(self.teacher_id)