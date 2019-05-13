from django.urls import path, include
from . import views

urlpatterns = [
    path('list', views.profile_detail, name='profile_detail'),
    path('new', views.profile_new, name='profile_new'),
]
