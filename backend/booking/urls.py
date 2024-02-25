from django.contrib import admin
from django.urls import path
from .views import (
  Weekly_reservation,
  Booking,
  ClassroomViewSet

)
urlpatterns = [
    path("weekly_reservation/",Weekly_reservation,name='予約一覧'),
    path('Booking/' ,Booking,name='予約表'),
    path('Classroom/', ClassroomViewSet.as_view({'get': 'list'}), name='教室番号'),
]