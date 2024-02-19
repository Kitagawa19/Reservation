from django.shortcuts import render
from .serializers import ClassroomSerializer,ClassroomReservationSerializer
from .models import Classroom,ClassroomReservation
from datetime import datetime,timedelta
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from accounts.models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def weekly_reservation(requeat,year,month,day):
  start_date=datetime(year,month,day).date()
  start_week=start_date-timedelta(days=start_date.weekday()+1)
  end_week=start_week+timedelta(days = 7)
  reservations=ClassroomReservation.objects.filter(date__rrange=(start_week,end_week))

  classroom_reservations = {}
  for reservation in reservations:
    if reservation.classroom_name not in classroom_reservations:
      classroom_reservations[reservation.classroom_name] = []
    classroom_reservations[reservation.classroom_name].append({
        'date':reservation.date,
        'start_time':reservation.start_time,
        'end_time':reservation.end_time,
        'purpose':reservation.purpose
    })
    return Response(classroom_reservations)
