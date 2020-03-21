from django.urls import path
from . import viewsf
urlpatterns =[path("",viewsf.index, name="index")]