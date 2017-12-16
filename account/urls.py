from django.conf.urls import url, include

from account import views


urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^update/$', views.update),
    url(r'^contact_info/$', views.contact_info),
]
