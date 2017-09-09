from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^about', views.about, name="about"),
    url(r'^compute_area', views.compute_area, name="compute_area"),
    url(r'^give_feedback', views.give_feedback, name="give_feedback"),
]
