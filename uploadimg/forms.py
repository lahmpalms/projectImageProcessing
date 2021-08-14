from django import forms
from django.forms import fields
from uploadimg.models import Image, Patient, Care, Nurse

class ImageForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields = ('patient_id', 'image','title')

class add_patient_form(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('patient_id', 'first_name', 'last_name', 'gender', 'birthday', 'HealthWelfare')

class add_care_form(forms.ModelForm):
    class Meta:
        model = Care
        fields = ('patient_id', 'care_date', 'lesion_id', 'nurse_id', 'detail' , 'image')

class add_nurse_form(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = ('nurse_id', 'first_name', 'last_name', 'gender', 'birthday')