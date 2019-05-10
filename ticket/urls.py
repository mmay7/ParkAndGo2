from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ticket_home, name='ticket_home'),
    path('list', views.tickets_list, name='tickets_list'),
    path('ticket/<int:pk>/', views.ticket_detail, name='ticket_detail'),
    path('ticket/search', views.ticket_search, name='ticket_search'),
    path('ticket/new', views.ticket_new, name='ticket_new'),
]
