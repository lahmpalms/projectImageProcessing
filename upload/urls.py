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
    path('add_patient/',views.add_patients, name='add_patient'),
    path('manage_patient/',views.manage_patient, name='manage_patient'),
    path('add_nurse/',views.add_nurse, name='add_nurse'),
    path('manage_nurse/',views.manage_nurse, name='manage_nurse'),
    # path('update_nurse/',views.update_nurse, name='update_nurse'),
    path('search/',views.search, name='search_data'),
    path('care/',views.add_care, name='add_care'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)