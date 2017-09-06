from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^compute_area', views.compute_area, name="compute_area"),
]
