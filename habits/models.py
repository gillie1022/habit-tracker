from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models import User
# Create your models here.


class Habit(models.Model):
    user = models.ForeignKey(to=User,
                             on_delete=models.CASCADE,
                             related_name="habits")
    # verb
    # noun
    # goal_quantity


class DailyRecord(models.Model):
    habit = models.ForeignKey(to=Habit,
                              on_delete=models.CASCADE,
                              related_name="records")
    # quantity