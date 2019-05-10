from django.urls import path, include
from . import views

urlpatterns = [
    path('list', views.profile_list, name='tickets_list'),
    path('info', views.profile_new, name='ticket_new'),
]
