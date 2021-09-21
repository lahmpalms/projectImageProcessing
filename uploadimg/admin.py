from django.contrib import admin

from .models import Image, Patient, HealthWelfare, Care, Lesion, LesionStatus, Nurse, Disease, frame

# Register your models here.

admin.site.register(Image)
admin.site.register(Patient)
admin.site.register(HealthWelfare)
admin.site.register(Care)
admin.site.register(Lesion)
admin.site.register(LesionStatus)
admin.site.register(Nurse)
admin.site.register(Disease)
admin.site.register(frame)