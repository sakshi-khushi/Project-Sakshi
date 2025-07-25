from django.db import models
userTypeData =(
    ("Teacher","Teacher"),
    ("Student","Student")
)
# Create your models here.
class sakshi_lmsUser(models.Model):
    userId= models.AutoField(primary_key=True)
    userName = models.CharField(max_length=20)
    email= models.EmailField(unique=True)
    gender = models.CharField(max_length=10,null=True,blank=True)
    number=models.IntegerField(unique=True)
    password=models.CharField(max_length=20)
    userType=models.CharField(max_length=10, choices=userTypeData)
    

class sakshi_courseUpload(models.Model):
        courseUploadId=models.AutoField(primary_key=True)
        courseName=models.CharField(max_length=20)
        courseDescription=models.CharField(max_length=50)
        createdAt=models.IntegerField()
        coursePlaylist=models.IntegerField()
        courseDuration=models.CharField(max_length=10)
        useName=models.ForeignKey(sakshi_lmsUser,on_delete=models.CASCADE)


# Create your models here.
