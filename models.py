from django.db import models

# Create your models here.

class contact(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

class blog(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField()
    description = models.TextField()


class registeruser(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

class login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=30)