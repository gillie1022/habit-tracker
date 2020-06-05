from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models import User
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

class DailyRecord(models.Model):
    habit = models.ForeignKey(to=Habit,
                              on_delete=models.CASCADE,
                              related_name="records",)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    recorded_on = models.DateField(auto_now=True, null=True, blank=True)
    class Meta:
        unique_together = ['habit', 'recorded_on']

    def __str__(self):
        return f"{self.recorded_on}: {self.quantity}"