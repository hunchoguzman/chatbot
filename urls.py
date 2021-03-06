"""chat URL Configuration

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

from django.urls import include, re_path

from django.urls import path

from chat.views import ChatterBotAppView,ChatterBotApiView,index,signup

urlpatterns = [
    re_path('admin/', admin.site.urls),


    re_path(r'^$', index, name="home"),


    re_path('home/', index, name="home"),

    re_path('signup/',signup,name='register'),

    path('accounts/', include('django.contrib.auth.urls')),

    re_path(r'^chat/$', ChatterBotAppView.as_view(), name='main'),

    re_path(r'^chat/api/chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),
]

