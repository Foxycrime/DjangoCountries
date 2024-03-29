"""DjangoCountries URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import *
from django.views import *
from MainApp import views


urlpatterns = [
    path('', views.about),
    # path('about', include (MainApp.url),
    path('countries-list/', views.list),
    path('country/<str:country>', views.country_page),
    path('country/countries-list/', views.list),
    path('languages_list/', views.languages_list),
    path('countries-list/<str:language>', views.country),
    path('language/', views.country),
    # path('countries/', views.post_list),
]
