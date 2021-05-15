from django.db import models
from django.conf import settings
import uuid
from django import forms
from PIL import Image
import random
from django.contrib.auth.models import User


class Voterlist(models.Model):
    Voter=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,verbose_name='Username')
    # id=models.AutoField(primary_key=True,default=random.randint(1,100000000), verbose_name='ID',null=False)
    Phone=models.CharField(max_length=14)
    Date_of_Birth=models.CharField(max_length=20)
    Address=models.CharField(max_length=300)
    Gender=models.CharField(max_length=6)
    Province = models.CharField(max_length=50)
    Citizen_ID_Number=models.CharField(max_length=50)
    Voter_ID_Number=models.CharField(max_length=20)
    Photo_Candidate=models.ImageField(default='default.png',upload_to='profile_pics')
    Photo_Citizenship_Front = models.ImageField(upload_to='ctzn_frnt')
    Photo_Citizenship_Rare = models.ImageField(upload_to='ctzn_rer')
    Remark=models.CharField(max_length=10,default='Pending')
    Vote_Status = models.CharField(max_length=10, default='None')
    def __str__(self):
        return self.Citizen_ID_Number

    def save(self):
        super().save()
        img1=Image.open(self.Photo_Candidate.path)
        img2 = Image.open(self.Photo_Citizenship_Front.path)
        img3 = Image.open(self.Photo_Citizenship_Rare.path)
        img1.thumbnail((350,350))
        img1.save(self.Photo_Candidate.path)
        img2.thumbnail((400, 700))
        img2.save(self.Photo_Citizenship_Front.path)
        img3.thumbnail((400, 700))
        img3.save(self.Photo_Citizenship_Rare.path)
