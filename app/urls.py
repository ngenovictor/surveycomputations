from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('compute_area', views.compute_area, name="compute_area"),
    path('give_feedback', views.give_feedback, name="give_feedback"),
]