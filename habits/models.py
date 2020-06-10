from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models import User
from datetime import date
import datetime
# Create your models here.


class Habit(models.Model):
    user = models.ForeignKey(to=User,
                             on_delete=models.CASCADE,
                             related_name="habits")
    action = models.CharField(max_length=255, null=True, blank=True)
    goal_quantity = models.PositiveIntegerField(null=True, blank=True)
    unit_of_measure = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.action} {self.goal_quantity} {self.unit_of_measure} per day"


    def get_last_21_days(self):
        record_list = list(self.records.values('recorded_on', 'quantity'))
        if len(record_list) > 0:
            start_date = record_list[0]['recorded_on']
        else:
            start_date = date.today()
        days = []
        if len(days) == 21:
            start_date = date.today() - datetime.timedelta(days=21)
        current = start_date
        while current <= date.today():
            days.append(current)
            current += datetime.timedelta(days=1)   
        records = {record['recorded_on']: record['quantity'] for record in record_list}
        last_21_days = []
        for day in days:
            last_21_days.append({'recorded_on': day, 'quantity': records.get(day)})
        return last_21_days



class DailyRecord(models.Model):
    habit = models.ForeignKey(to=Habit,
                              on_delete=models.CASCADE,
                              related_name="records",)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    recorded_on = models.DateField(auto_now_add=True, null=True, blank=True)
    class Meta:
        unique_together = ['habit', 'recorded_on']

    def __str__(self):
        return f"{self.recorded_on}: {self.quantity}"

    def get_quantity(self):
        quantity = self.quantity
        return int(quantity)

