from django.db import models

# Create your models here.
class student(models.Model):
    Name=models.CharField(max_length=40)
    Rollno=models.CharField(max_length=10)
    Course=models.CharField(max_length=20)

    class Meta:
        db_table="student_table"