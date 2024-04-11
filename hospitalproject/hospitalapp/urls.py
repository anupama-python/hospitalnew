from django.contrib import admin
from django.urls import path, include

from hospitalapp import views

urlpatterns = [
    path('',views.base,name="base"),
    path('contact', views.contact, name="contact"),
    path('departments', views.departments, name="departments"),
    path('doctors',views.doctors,name='doctors'),
    path('aboutus',views.aboutus,name='aboutus'),
path('booking',views.booking,name='booking'),
    path('message',views.message,name='message'),
    path("history",views.history,name="history"),
]
