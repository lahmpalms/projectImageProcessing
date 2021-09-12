from django.db.models import query
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils.translation import deactivate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from upload.decorators import unauthenticated_user, allowed_users

from numpy.lib.type_check import imag
from uploadimg.forms import ImageForm ,add_patient_form, add_care_form, add_nurse_form, add_disease_form, add_disease_form, add_healthwelfare_form, CreateUserForm
from .models import Care, Nurse, Patient, Disease, HealthWelfare

from uploadimg.utils import Calculate , bitwise
from skimage.morphology import black_tophat, skeletonize, convex_hull_image

import PIL as Image
import numpy as np
import cv2
# Create your views here.


def index(request):

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            value = Calculate(img_obj.image.path)
            img_obj.img_value = value
            form.save()
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj, 'value':value})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def add_patients(request):
    if request.method == 'POST':
        add_patient = add_patient_form(request.POST)
        if add_patient.is_valid():
            add_patient.save()
            add_obj = add_patient.instance
            return render(request, 'add_patient.html',{'add_patient':add_patient, 'add_obj':add_obj})
    else:
        add_patient = add_patient_form()
    return render(request, 'add_patient.html',{'add_patient':add_patient})
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin', 'nurse'])
def add_care(request):
    if request.method == 'POST':
        add_care = add_care_form(request.POST, request.FILES)
        if add_care.is_valid():
            add_care.save()
            add_obj = add_care.instance
            value = Calculate(add_obj.image.path)
            add_obj.size = value
            add_care.save()
            return render(request, 'add_care.html',{'add_care':add_care, 'add_obj' : add_obj})
    else:
        add_care = add_care_form()
    return render(request, 'add_care.html',{'add_care':add_care})
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def add_nurse(request):
    if request.method == 'POST':
        add_nurse = add_nurse_form(request.POST)
        if add_nurse.is_valid():
            add_nurse.save()
            add_obj = add_nurse.instance
            return render(request, 'add_nurse.html',{'add_nurse':add_nurse, 'add_obj':add_obj})
    else:
        add_nurse = add_nurse_form

    return render(request, 'add_nurse.html',{'add_nurse':add_nurse})
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def add_disease(request):
    if request.method == 'POST':
        add_disease = add_disease_form(request.POST)
        if add_disease.is_valid():
            add_disease.save()
            add_obj = add_disease.instance
            return render(request, 'add_disease.html', {'add_disease':add_disease, 'add_obj':add_obj})
    else:
        add_disease = add_disease_form
    return render(request, 'add_disease.html',{'add_disease':add_disease})
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def add_healthWelfare(request):
    if request.method == 'POST':
        add_healthwelfare = add_healthwelfare_form(request.POST)
        if add_healthwelfare.is_valid():
            add_healthwelfare.save()
            add_obj = add_healthwelfare.instance
            return render(request, 'add_healthwelfare.html', {'add_healthwelfare':add_healthwelfare, 'add_obj':add_obj})
    else:
        add_healthwelfare = add_healthwelfare_form
    return render(request, 'add_healthwelfare.html',{'add_healthwelfare':add_healthwelfare})
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def manage_nurse(request):
    results = Nurse.objects.all()
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            search_results = Nurse.objects.filter(first_name__contains = query_name)
            return render(request, 'manage_nurse.html', {'results':search_results})
    return render(request, 'manage_nurse.html', {'results':results})
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def manage_patient(request):
    results = Patient.objects.all()
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            search_results = Patient.objects.filter(first_name__contains = query_name)
            return render(request, 'manage_patient.html', {'results':search_results})
    return render(request, 'manage_patient.html', {'results':results})
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def manage_disease(request):
    results = Disease.objects.all()
    return render(request, 'manage_disease.html', {'results':results})
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def manage_healthWelfare(request):
    results = HealthWelfare.objects.all()
    return render(request, 'manage_healthwelfare.html', {'results':results})
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin', 'nurse'])
def search(request):
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Care.objects.filter(patient_id__first_name__contains=query_name)
            return render(request, 'show_data.html', {"results":results})

    return render(request, 'show_data.html')

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def updateNurse(request, nurse_id):
    nurse = Nurse.objects.get(nurse_id = nurse_id)
    form = add_nurse_form(instance=nurse)
    if request.method == 'POST':
        form = add_nurse_form(request.POST, instance=nurse)
        if form.is_valid():
            form.save()
            return redirect('manage_nurse')
    return render(request, 'edit_nurse.html', {'form':form})
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def deleteNurse(request, nurse_id):
    nurse = Nurse.objects.get(nurse_id = nurse_id)
    context = {'delete_obj':nurse}
    if request.method == 'POST':
        nurse.delete()
        return redirect('manage_nurse')
    return render(request, 'delete_nurse.html', context)
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def updatePatient(request, patient_id):
    patient = Patient.objects.get(patient_id = patient_id)
    form = add_patient_form(instance=patient)
    if request.method == 'POST':
        form = add_patient_form(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('manage_patient')
    return render(request, 'edit_patient.html', {'form':form})
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def deletePatient(request, patient_id):
    patient = Patient.objects.get(patient_id = patient_id)
    context = {'delete_obj':patient}
    if request.method == 'POST':
        patient.delete()
        return redirect('manage_patient')
    return render(request, 'delete_patient.html', context)
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def updateDisease(request, Disease_id):
    disease = Disease.objects.get(Disease_id = Disease_id)
    form = add_disease_form(instance=disease)
    if request.method == 'POST':
        form = add_disease_form(request.POST, instance=disease)
        if form.is_valid():
            form.save()
            return redirect('manage_disease')
    return render(request, 'edit_disease.html', {'form':form})
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def deleteDisease(request, Disease_id):
    disease = Disease.objects.get(Disease_id = Disease_id)
    context = {'delete_obj':disease}
    if request.method == 'POST':
        disease.delete()
        return redirect('manage_disease')
    return render(request, 'delete_disease.html', context)
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def updateHealthwelfare(request, HealthWelfare_ID):
    healthwelfare = HealthWelfare.objects.get(HealthWelfare_ID = HealthWelfare_ID)
    form = add_healthwelfare_form(instance=healthwelfare)
    if request.method == 'POST':
        form = add_healthwelfare_form(request.POST, instance=healthwelfare)
        if form.is_valid():
            form.save()
            return redirect('manage_healthwelfare')
    return render(request, 'edit_healthwelfare.html', {'form':form})
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def deleteHealthwelfare(request, HealthWelfare_ID):
    healthwelfare = HealthWelfare.objects.get(HealthWelfare_ID = HealthWelfare_ID)
    context = {'delete_obj':healthwelfare}
    if request.method == 'POST':
        healthwelfare.delete()
        return redirect('manage_healthwelfare')
    return render(request, 'delete_healthwelfare.html', context)

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form' : form}
    return render (request, 'register.html',context)
@unauthenticated_user
def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect ('add_care')
        else:
            messages.info(request, 'Username or Password inccorrect!!')
            
    context = {}
    return render (request, 'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('index')

def AdminloginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect ('AdminPage')
        else:
            messages.info(request, 'Username or Password inccorrect!!')
            
    context = {}
    return render (request, 'admin_login.html',context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def AdminPage(request):

    return render(request, 'admin_page.html')