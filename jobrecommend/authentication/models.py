from django.db import models

class register1(models.Model):
    name=models.CharField(max_length=100,blank=False)
    email=models.TextField(max_length=700,blank=False)
    password=models.TextField(max_length=700,blank=False)
