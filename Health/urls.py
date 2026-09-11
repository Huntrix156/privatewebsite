"""
URL configuration for DenisPrivatewebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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

from Health import views

urlpatterns = [
  path('',views.Add_record,name='Add_record'),
  path('Emergency_contact',views.Emergency_contact,name='Emergency_contact'),
  path('Record_details/',views.Record_details,name='Record_details'),
  path('',views.Record_list,name='Record_list'),
]
