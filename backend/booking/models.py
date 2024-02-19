from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

#教室のモデル
class Classroom(models.Model):
  name = models.CharField(max_length=100)
  def __str__(self):
    return self.name

#予約のモデル
class ClassroomReservation(models.Model):
    user = models.ForeignKey('accounts.CustomUser',on_delete=models.CASCADE)
    classroom_name = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    purpose = models.TextField()
    def __str__(self):
      return self.classroom_name 
    
    def cleen(self):
      if self.start_time >= self.end_time:
        raise ValidationError('開始時間は終了時間よりも後になっています。')
      
      overlapping_reservations = ClassroomReservation.objects.filter(
        classroom_name=self.classroom_name,
        date=self.date,
        start_time__lt=self.end_time,
        end_time__gt=self.start_time
      ).exclude(usrt=self.user)

      if overlapping_reservations.exists():
        raise ValidationError('この時間帯はすでに予約されています。')
    
    def save(self,*args,**kwargs):
      self.full_clean()
      super().save(*args,**kwargs)