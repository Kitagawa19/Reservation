from rest_framework import serializers
from .models import Classroom,ClassroomReservation

class ClassroomSerializer(serializers.ModelSerializer):
  class Meta:
    model = Classroom
    fields = '__all__'


class ClassroomReservationSerializer(serializers.ModelSerializer):
  class Meta:
    model = ClassroomReservation
    fields = '__all__'