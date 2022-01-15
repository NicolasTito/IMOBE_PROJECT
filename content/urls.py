from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('property/<str:id>', views.property, name="property"),
    path('schedule_visits', views.schedule_visits, name="schedule_visits"),
    path('schedules', views.schedules, name="schedules"),
    path('cancel_schedules/<str:id>', views.cancel_schedule, name="cancel_schedule")
]

