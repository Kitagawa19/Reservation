from django.contrib import admin
from django.urls import path
from .views import (
  Weekly_reservation,
  Booking,
  ClassroomViewSet
)

urlpatterns = [
    path("weekly_reservation/",Weekly_reservation,name='weekly_reservation'),
    path('ClassroomReservation/' ,Booking,name='classroom_reservation'),
    path('Classroom',ClassroomViewSet.as_view(),name='Classroom'),
]