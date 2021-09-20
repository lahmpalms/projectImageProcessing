from django.urls import path
from uploadimg import views

urlpatterns = [
    path('', views.chart, name = 'dashboard'),
    path('bubble/', views.chart, name = 'dashboard2'),
]
