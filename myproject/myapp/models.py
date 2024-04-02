from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=255)

class Subject(models.Model):
    name = models.CharField(max_length=100)

class Chair(models.Model):
    name = models.CharField(max_length=100)

class Lecturer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    chair = models.ForeignKey(Chair, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)

class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    date = models.DateField()
    mark = models.DecimalField(max_digits=5, decimal_places=2)
