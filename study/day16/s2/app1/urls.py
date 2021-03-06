"""s2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from app1 import views

urlpatterns = [

    # url(r'^moblea/', include("app1.urls")),
    # url(r'^moblea/', include("app2.urls")),
    # # # url(r'^home/', views.Home.as_view()),
    url(r'^home/', views.home),
    # url(r'^login', views.login),
    # url(r'^detail-(?P<uid>\d+).html', views.detail, name="dex"),
]
