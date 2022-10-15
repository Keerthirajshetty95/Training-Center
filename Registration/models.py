from django.db import models

# Create your models here.
class Course(models.Model):
    course_ID = models.CharField(max_length=264, unique=True)
    course_name = models.CharField(max_length=264)
    def __str__(self):
        return self.course_ID



class Batch(models.Model):
    batch_ID = models.CharField(max_length=264, unique=True)
    course_ID = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return self.batch_ID

class Student(models.Model):
    student_ID = models.CharField(max_length=264, unique=True)
    student_name = models.CharField(max_length=264)
    course_ID = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch_ID = models.ForeignKey(Batch, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=264)
    branch = models.CharField(max_length=264)
    year = models.CharField(max_length=264)
    experience = models.CharField(max_length=264)
    url = models.URLField()
    def __str__(self):
        return self.student_name
