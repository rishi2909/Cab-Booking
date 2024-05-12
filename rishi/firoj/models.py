from django.db import models

# Create your models here.
#model for signpform
class customersignupform(models.Model):
    CName=models.CharField(max_length=50)
    CEmail=models.CharField(max_length=20)
    pwd=models.CharField(max_length=50)
    db_table="customersignupform"

#model fo availableCab
class availablecab(models.Model):
        DName=models.CharField(max_length=50)
        CNo=models.CharField(max_length=10)
        DphNo=models.CharField(max_length=10)
        CType=models.CharField(max_length=10)
        db_table="availablecab"

class customer(models.Model):
      CName=models.CharField(max_length=50)
      CAddress=models.CharField(max_length=50)       
      CphNo=models.CharField(max_length=12)
      CEmail=models.CharField(max_length=20)
      db_table="customer"