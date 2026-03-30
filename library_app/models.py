from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username} ({self.roll_number})"

class IssuedBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(default=date.today() + timedelta(days=14))

    def __str__(self):
        return f"{self.book.title} issued to {self.student.user.username}"