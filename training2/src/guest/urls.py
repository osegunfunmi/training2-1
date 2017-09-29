from django.conf.urls import url
from src.guest import views


urlpatterns = [
    # GUEST MODULE URLs
    url(r'^guest/$', views.guest,),
    url(r'^guest/(?P<method>[-\w+]+)/$', views.guest),
    url(r'^guest/(?P<method>[-\w+]+)/(?P<pk>\d+)/$', views.guest),

    # EVENT MODULE URLS
    #url(r'^event/$', views.event),
    #url(r'^event/(?P<method>[-\w+]+)/$', views.event),
    #url(r'^eventt/(?P<method>[-\w+]+)/(?P<pk>\d+)/$', views.event),
]
