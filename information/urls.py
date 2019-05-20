from django.urls import path
from . import views

urlpatterns = [
    path('user', views.profile_search, name='profile_search'),
    path('new', views.profile_new, name='profile_new'),
]
