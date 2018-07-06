from django.urls import path
from django.conf.urls import include
from .import views

urlpatterns = [
    path(r'', views.index, name ='index'), #links to index funciton in views.py
    path(r'contact/', views.contact, name ='contact'),
]
