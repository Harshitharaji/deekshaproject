from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from ckeditor.fields import RichTextField
# Create your models here.
class Assessment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='questions')
    Questiontext = RichTextField()
    option1 = models.CharField(max_length=1000)
    option2 = models.CharField(max_length=1000)
    option3 = models.CharField(max_length=1000,null=True,blank=True)
    option4 = models.CharField(max_length=1000,null=True,blank=True)
    options=(
        ('option1',option1),
        ('option2',option2),
        ('option3',option3),
        ('option4',option4)
    )
    topic=models.CharField(max_length=500,default="which topic this question comes from")
    answer = models.CharField(max_length=1000,choices=options)

    def __str__(self):
        return self.Questiontext
    
class AssessmentResults(models.Model):
    user=models.EmailField()
    courseTitle=models.CharField(max_length=200)
    obtainedScore=models.IntegerField()
    score=models.IntegerField()
    percentageObtained=models.IntegerField(blank=True,null=True)
    result=models.CharField(max_length=50,blank=True,null=True)
    improvementPlans=models.TextField(max_length=5000,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.created_at.strftime('%d-%m-%Y')
    
class Profile(models.Model):
    _id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=150)
    profilepic=models.ImageField(upload_to="profile",blank=True,null=True)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15)
    alternateNumber=models.CharField(max_length=15,blank=True,null=True)
    address=models.TextField(max_length=500)
    schoolName=models.CharField(max_length=500)
    xpercentage=models.IntegerField()
    xcourse=models.TextField(max_length=500)
    xdate=models.CharField(max_length=100)
    xcity=models.CharField(max_length=100)
    collegeName=models.CharField(max_length=300)
    xiipercentage=models.IntegerField()
    xiicourse=models.TextField(max_length=500)
    xiidate=models.CharField(max_length=100)
    xiicity=models.CharField(max_length=100)
    universityName=models.TextField(max_length=300)
    universitypercentage=models.IntegerField()
    branch=models.CharField(max_length=200)
    startdate=models.CharField(max_length=100)
    enddate=models.CharField(max_length=100)
    universitycity=models.CharField(max_length=100,blank=True,null=True)
    muniversityName=models.TextField(max_length=300,blank=True,null=True)
    muniversitypercentage=models.CharField(max_length=100,blank=True,null=True)
    mbranch=models.CharField(max_length=200,blank=True,null=True)
    mstartdate=models.CharField(max_length=100,blank=True,null=True)
    menddate=models.CharField(max_length=100,blank=True,null=True)
    muniversitycity=models.CharField(max_length=100,blank=True,null=True)
    skills=models.TextField(max_length=500)
    p1=models.CharField(max_length=100,blank=True,null=True)
    p1d=models.TextField(max_length=500,blank=True,null=True)
    p1l=models.TextField(max_length=500,blank=True,null=True)
    p2=models.CharField(max_length=100,blank=True,null=True)
    p2d=models.TextField(max_length=500,blank=True,null=True)
    p2l=models.TextField(max_length=500,blank=True,null=True)
    i1=models.CharField(max_length=100,blank=True,null=True)
    i1d=models.TextField(max_length=500,blank=True,null=True)
    i2=models.CharField(max_length=100,blank=True,null=True)
    i2d=models.TextField(max_length=500,blank=True,null=True)
    github=models.TextField(max_length=500,blank=True,null=True)
    linkedin=models.TextField(max_length=500,blank=True,null=True)
    facebook=models.TextField(max_length=500,blank=True,null=True)
    instagram=models.TextField(max_length=500,blank=True,null=True)
    role=models.CharField(max_length=150,blank=True,null=True)
    summary=models.TextField(max_length=500,blank=True,null=True)
    timeStamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.name
    

class Certifications(models.Model):
    cid=models.AutoField(primary_key=True)
    email=models.EmailField()
    name=models.CharField(max_length=100,blank=True,null=True)
    courseName=models.CharField(max_length=150,blank=True,null=True)
    courseScore=models.CharField(max_length=150,blank=True,null=True)
    courseCertificate=models.ImageField(upload_to="profile",blank=True,null=True)
    
    def __str__(self):
        return self.email


class AdvisorSupportTask(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=100)
    taskName=models.CharField(max_length=100)
    taskDescription=models.TextField(max_length=500)
    taskAssignedby=models.ForeignKey(User, on_delete=models.CASCADE)
    taskCompleted=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


