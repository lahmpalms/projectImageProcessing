from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case
from django.utils import timezone

# Create your models here.

class Disease(models.Model):
    Disease_id = models.CharField(max_length = 5)
    Disease_name = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.Disease_name
    

class HealthWelfare(models.Model):
    HealthWelfare_ID = models.CharField(max_length=3)
    HealthWelfare_name = models.CharField(max_length=50)

    def __str__(self):
        return self.HealthWelfare_ID + " " + self.HealthWelfare_name

class LesionStatus(models.Model):
    lesion_statusid = models.CharField(max_length=4)
    lesion_statusname = models.CharField(max_length=200)
    def __str__(self):
        return self.lesion_statusid + " " + self.lesion_statusname

class Patient(models.Model):
    GENDER_CHOICES = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE')
    )
    patient_id = models.CharField(max_length=8)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
    birthday = models.DateField()
    age = models.IntegerField(null = True)
    Disease_id = models.ForeignKey (Disease, null = True, on_delete = CASCADE)
    HealthWelfare = models.ForeignKey(HealthWelfare,null=True ,on_delete= CASCADE)
    def __str__(self):
        return self.patient_id + " " + self.first_name + " " + self.last_name

class Nurse(models.Model):
    GENDER_CHOICES = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE')
    )
    nurse_id = models.CharField(max_length=8, primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
    birthday = models.DateField()

    def __str__(self):
        return self.nurse_id + " " + self.first_name + " " + self.last_name

class Care(models.Model):
    
    patient_id = models.ForeignKey(Patient, null=True,on_delete= CASCADE)
    care_date = models.DateField(default=timezone.now)
    lesion_id = models.CharField(max_length=5,primary_key=True)
    nurse_id = models.CharField(max_length=8)
    detail = models.TextField()
    lesion_statusid = models.ForeignKey(LesionStatus, null=True, on_delete=CASCADE)
    image = models.ImageField()
    size = models.IntegerField(default=0)

    def __str__(self):
        return  self.lesion_id+"  "+str(self.patient_id)

class Lesion(models.Model):
    lesion_id = models.CharField(max_length=5,primary_key=True)
    lesiondetail = models.TextField(max_length=200)
    lesion_statusid = models.ForeignKey(LesionStatus, null=True, on_delete=CASCADE)
    patient_id = models.ForeignKey(Patient, null=True, on_delete=CASCADE,related_name='lesionPatient')

    def __str__(self):
        return self.lesion_id

class Image(models.Model):
    patient_id = models.ForeignKey(Patient, null=True , on_delete=CASCADE , related_name= 'imagePatient')
    image = models.ImageField(upload_to='images')
    title = models.TextField()
    img_value = models.IntegerField(default=0)



    def __str__(self):
        return str(self.patient_id) + " "  + " IMAGE VALUE IS : " + str(self.img_value)
        # show name in admin

    class Meta:
        db_table = 'myapp_image'
