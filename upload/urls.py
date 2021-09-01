"""upload URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from uploadimg import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    #patient
    path('add_patient/',views.add_patients, name='add_patient'),
    path('manage_patient/',views.manage_patient, name='manage_patient'),
    path('update_patient/<str:patient_id>',views.updatePatient, name='update_patient'),
    path('delete_patient/<str:patient_id>',views.deletePatient, name='delete_patient'),
    
    #nurse
    path('add_nurse/',views.add_nurse, name='add_nurse'),
    path('manage_nurse/',views.manage_nurse, name='manage_nurse'),
    path('update_nurse/<str:nurse_id>',views.updateNurse, name='update_nurse'),
    path('delete_nurse/<str:nurse_id>',views.deleteNurse, name='delete_nurse'),
    
    path('search/',views.search, name='search_data'),
    path('care/',views.add_care, name='add_care'),
    
    #disease
    path('add_disease/',views.add_disease, name='add_disease'),
    path('manage_disease/',views.manage_disease, name='manage_disease'),
    path('update_disease/<str:Disease_id>',views.updateDisease, name='update_disease'),
    path('delete_disease/<str:Disease_id>',views.deleteDisease, name='delete_disease'),
    
    #healthwelfare
    path('add_healthwelfare/',views.add_healthWelfare, name='add_healthwelfare'),
    path('manage_healthwelfare/',views.manage_healthWelfare, name='manage_healthwelfare'),
    path('update_healthwelfare/<str:HealthWelfare_ID>',views.updateHealthwelfare, name='update_healthwelfare'),
    path('delete_healthwelfare/<str:HealthWelfare_ID>',views.deleteHealthwelfare, name='delete_healthwelfare'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)