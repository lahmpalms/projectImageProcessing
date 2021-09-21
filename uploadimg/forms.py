from django import forms
from django.forms import fields
from uploadimg.models import Image, Patient, Care, Nurse, Disease, HealthWelfare, frame
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
class ImageForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields = ('patient_id', 'image','title')

class add_patient_form(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('patient_id', 'first_name', 'last_name', 'gender', 'birthday', 'Disease_id', 'HealthWelfare')

class add_care_form(forms.ModelForm):
    class Meta:
        model = Care
        fields = ('patient_id', 'care_date', 'lesion_id', 'nurse_id', 'detail' , 'lesion_statusid', 'image', 'frame')

class add_nurse_form(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = ('nurse_id', 'first_name', 'last_name', 'gender', 'birthday')
        
class add_disease_form(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ('__all__')
        
class add_healthwelfare_form(forms.ModelForm):
    class Meta:
        model = HealthWelfare
        fields = ('__all__')
        
class add_frame_form(forms.ModelForm):
    class Meta:
        model = frame
        fields = ('__all__')