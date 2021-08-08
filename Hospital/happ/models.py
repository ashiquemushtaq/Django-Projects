from django.db import models

# Create your models here.
from django.urls import reverse


class department(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    def __str__(self):
        return self.name

class doctor(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    dep = models.ForeignKey(department,on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    img = models.ImageField(upload_to='doctors')
    def __str__(self):
        return self.name

class patient(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    doctor = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    def __str__(self):
        return self.name