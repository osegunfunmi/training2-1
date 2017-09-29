"""training2 URL Configuration

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

from src.guest import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^guestapp/', include('src.guest.urls')),
    #url(r'^guestapp/', include('src.event.urls')),
    url(r'^event/$', views.event, name='event'),
    url(r'^update/(?P<method>[-\w+]+)/(?P<pk>\d+)/$', views.guest, name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name='delete'),
]

