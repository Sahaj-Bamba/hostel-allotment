from django.urls import re_path
from . import views

app_name = 'base'

urlpatterns = [
    re_path(r'home/', views.home, name='home'),
    re_path(r'contact/', views.contact, name='contact'),
    re_path(r'^[?]*', views.not_found, name='not_found'),
]
