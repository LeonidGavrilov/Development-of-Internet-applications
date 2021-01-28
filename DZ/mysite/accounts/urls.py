from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
# from django.contrib.auth import views
from . import views

urlpatterns = [
    # post views
    # path('login/', views.user_login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    # url(r'^login/$', views.user_login, name='login'),
]