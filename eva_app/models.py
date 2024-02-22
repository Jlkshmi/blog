from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_publisher=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=False)

class Customer(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()

class Publisher(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    upload_pic = models.FileField(upload_to='documents/')
