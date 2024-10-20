
from django.db import models

class Student(models.Model):
    rollno = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name
    

    # crudapp/models.py
