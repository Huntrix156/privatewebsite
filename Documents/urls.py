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

from Documents import views

urlpatterns = [
    path('Add_page/',views.Add_page,name='Add_page'),
    path('Detail_page/',views.Detail_page,name='Detail_page'),
    path('Edit_page/',views.Edit_page,name='Edit_page'),
    path('list_page',views.list_page,name='list_page'),
    path('Index/',views.index,name='index'),
    path('about/',views.about,name='about'),
]
