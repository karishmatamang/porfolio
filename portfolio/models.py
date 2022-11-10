from distutils.command.upload import upload
from django.db import models
from django.forms import CharField


# Create your models here.

class PersonalPorfolio(models.Model):
    firstname=models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    profession=models.CharField(max_length=250,null=True,blank=True)
    email=models.CharField(max_length=250)    
    contact=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    profile=models.ImageField(upload_to='image',null=True,blank=True)
    # updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname

class Skills(models.Model):
    title=models.CharField(max_length=250)
    score=models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.title

class ProfessionalSkill(models.Model):
    title=models.CharField(max_length=250)
    score=models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.title

class EducationDegree(models.Model):
    college=models.CharField(max_length=250)
    level=models.CharField( max_length=50)
    faculty=models.CharField(max_length=50)
    score=models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.college

class Hobby(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Experience(models.Model):
    companyname=models.CharField(max_length=250)
    workdone=models.TextField(null=True,blank=True)
    startdate=models.DateField(null=True,blank=True)
    enddate=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.companyname