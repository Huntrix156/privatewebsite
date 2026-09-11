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
from django.urls import path

from Journal import views

urlpatterns = [
    path('Add_Journal/',views.Add_Journal,name='Add_Journal'),
    path('Delete_Journal/',views.Delete_Journal,name='Delete_journal'),
    path('Edit_Journal',views.Edit_Journal,name='Edit_journal'),
    path('Journal_details/',views.Journal_details,name='Journal_details'),
]
