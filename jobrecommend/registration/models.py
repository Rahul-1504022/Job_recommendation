from django.db import models

# Create your models here.

class userregistration(models.Model):
    fullname = models.CharField(max_length=200,blank=False)
    email = models.EmailField(max_length = 254,blank=False)
    password = models.CharField(max_length=200,blank=False)
    confirmpassword = models.CharField(max_length=50,blank=False)


    def __str__(self):
        return self.fullname


class userprofile(models.Model) :
    username = models.CharField(max_length=200,blank=False)
    email = models.EmailField(max_length = 254,blank=False)
    fullname = models.CharField(max_length=200,blank=False)
    aboutyourself = models.CharField(max_length=1000,blank=False)
    gender = models.CharField(max_length=100,blank=False)
    degree = models.CharField(max_length=100,blank=False)
    subject = models.CharField(max_length=100,blank=False)
    presentjobdesignation = models.CharField(max_length=2000,blank=False)
    pastjobdesignation = models.CharField(max_length=2000,blank=False)
    fieldofinterest = models.CharField(max_length=100,blank=False)
    contactno = models.CharField(max_length=100,blank=False)    
    permanentaddress = models.CharField(max_length=2000,blank=False)
    presentaddress = models.CharField(max_length=2000,blank=False)

    def __str__(self):
        return self.fullname

class usercv(models.Model):
    username = models.CharField(max_length=200,blank=False)
    cv = models.FileField(upload_to='cv/',blank=False)


    def __str__(self):
        return self.username