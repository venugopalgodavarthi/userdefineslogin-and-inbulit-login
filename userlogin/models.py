from django.db import models

# Create your models here.
class login(models.Model):
    firstname= models.CharField(max_length=25)
    lastname= models.CharField(max_length=25)
    email= models.EmailField(max_length=25,unique=True)
    phone= models.BigIntegerField(unique=True)
    password= models.CharField(max_length=25)
    repassword= models.CharField(max_length=25)
