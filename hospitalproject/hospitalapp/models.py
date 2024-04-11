from django.db import models

# Create your models here.
class Departments(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField(max_length=250)
    image=models.ImageField(upload_to='images')
    def __str__(self):
        return self.name
class Doctors(models.Model):
    name_doc=models.CharField(max_length=250)
    dep=models.TextField(max_length=250)
    image=models.ImageField(upload_to='images')
    def __str__(self):
        return self.name_doc