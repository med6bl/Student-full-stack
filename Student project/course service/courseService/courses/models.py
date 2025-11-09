from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    schedule = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('student', 'course')
