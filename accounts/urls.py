from django.urls import path,re_path

from . import views

app_name='accounts'

urlpatterns = [
    re_path(r'^signup/$', views.user_signup, name='signup'),
    re_path(r'^login/$', views.user_login, name='login'),
    re_path(r'^logout/$',views.user_logout, name='logout'),
    re_path(r'^profile/$',views.user_profile, name='profile'),
    re_path(r'^team/$',views.team, name='team'),
    re_path(r'^validate/$',views.validate, name='validate'),
    re_path(r'^request/$', views.requests, name='requests'),
    re_path(r'^professor/$', views.proff, name='proff'),
]