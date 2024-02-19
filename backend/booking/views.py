from django.shortcuts import render
from .serializers import ClassroomSerializer,ClassroomReservationSerializer
from .models import Classroom,ClassroomReservation
from datetime import datetime,timedelta
from rest_framework.decorators import api_view,permission_classes
from django.http import JsonResponse
from accounts.models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
#全体の予約状況のリストの作成
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
    return JsonResponse(classroom_reservations)
@csrf_exempt
@permission_classes([IsAuthenticated])
@api_view(['POST','GET'])
#予約の作成
def booking(request):
  if request.method == 'POST':
    username = request.data.get('username')
    user_instance = CustomUser.objects.get(username=username)
    Classroom_name = request.data.get('classroom_name') 
    Date = request.data.get('date') 
    Staet_time = request.data.get('start_time') 
    End_time = request.data.get('end_time') 
    Purpose = request.data.get('purpose') 
    ClassroomReservation.objects.create(
      user=user_instance,
      classroom_name=Classroom_name,
      date=Date,start_time=Staet_time,
      end_time=End_time,
      purpose=Purpose)
    return JsonResponse({'message':'予約が完了しました'})
#予約のマイリストの取得
  elif request.method == 'GET':
    my_reservation = ClassroomReservation.objects.all(filter(user=request.user))
    reservation_list = []
    for reservation in my_reservation:
      try:
        reservation_list.append({
          'classroom_name':reservation.classroom_name,
          'date':reservation.date,
          'start_time':reservation.start_time,
          'end_time':reservation.end_time,
          'purpose':reservation.purpose
        })
      except reservation.DoesNotExist:
        pass
#safe=Falseで辞書型ではないデータも返せるようになる
      return JsonResponse(reservation_list,safe=False)
    else:
      return JsonResponse({'message':'予約がありません'})