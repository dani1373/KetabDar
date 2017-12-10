from django.conf.urls import url, include

from account import views


urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^update/$', views.update),
]
