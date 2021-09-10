from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Patient(models.Model) :
   
    User = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    patient_name = models.CharField(max_length=200,null=True,blank=True)
    patient_age = models.IntegerField(null=True,blank= True)
    Education = models.CharField(max_length=100,null=True,blank=True)
    Occupation =models.CharField(max_length=100,null=True,blank=True)
    mr_choice=(
       ( 'Married' ,'Married'),
       ( 'Unmarried' ,'Unmarried'),
       ( 'Not willing to disclose' ,'Not willing'),
    )
    Marital_status= models.CharField(max_length=100,blank=True,null=True,choices=mr_choice)
    Address =models.CharField(max_length=200,null=True,blank=True)
    Mobile_no = models.CharField(max_length=200,null=True,blank=True)
    alt_no =models.CharField(max_length=200,null=True,blank=True)
    Email_address = models.CharField(max_length=200,null=True,blank=True)
    Presenting_Compliance = models.TextField(null=True,blank=True)
    clinical_conditions=(
       ( 'DM' ,'DM'),
       ( 'HTN' ,'HTN'),
       ( 'HIPOTHYROIDISM','HIPOTHYROIDISM'),
        ( 'HYPERLIPIDIMIA','HYPERLIPIDIMIA'),
        ( 'HEARTCONDITIONS','HEARTCONDITIONS'),
    )
    Clinical_Conditions =models.CharField(max_length=100,blank=True,null=True,choices=clinical_conditions)
    Family_History = models.CharField(max_length=200,null=True,blank=True)
    Past_History = models.CharField(max_length=200,null=True,blank=True)
    Personal_History =models.CharField(max_length=200,null=True,blank=True)
    Lifespace_Investigation =models.CharField(max_length=200,null=True,blank=True)
    Case_Analysis =models.CharField(max_length=200,null=True,blank=True)
    create =models.DateTimeField(auto_now_add=True)



    def __str__(self) : 
        return self.patient_name
    
    class Meta :
        ordering = ['patient_name']

