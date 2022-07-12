from pickle import GLOBAL
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

class Habit(models.Model):
    habit_name = models.CharField(max_length=255)
    goal = models.PositiveIntegerField()

class Date(models.Model):
    date = models.DateField()
    tracked_habits = models.ManyToManyField("Habit", related_name="tracked_habits")
    habit_status = models.PositiveIntegerField()