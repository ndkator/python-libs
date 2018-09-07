"""acer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from controlcenter.views import controlcenter
from django.urls import path, include, re_path
from boom import views

# Главный конструктор URL адресов. Определяет что происходит при переходе на каждый из разделов, указанных ниже.

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about),
    path('admin/', admin.site.urls),
    path('admin/dashboard/', controlcenter.urls),
    path('modules/', include('basetest.urlsmodule')),
    path('creators/', include('basetest.urlscreator')),
    path('libs/', include('basetest.urlslib')),
    path('tasks/', include('basetest.urlstask')),
    path('accounts/', include('allauth.urls')),
    path('search/', views.search),
]
