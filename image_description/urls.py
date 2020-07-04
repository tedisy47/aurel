
from django.contrib import admin
from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^upload_image', views.upload_image)

]
