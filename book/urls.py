from django.conf.urls import url, include

from book import views


urlpatterns = [
    url(r'^update/$', views.update),
    url(r'^view_list/$', views.view_list),
    url(r'^info/$', views.info),
]
