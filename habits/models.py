from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.constraints import UniqueConstraint


# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return self.username

class Habit(models.Model):
    habit_name = models.CharField(max_length=255, null=True, blank=True)
    goal = models.PositiveIntegerField(null=True, blank=True)
    metric = models.CharField(max_length=255, null=True, blank=True)
    creator = models.ForeignKey("User", on_delete=models.SET_NULL, related_name='creator', null=True, blank=True)

class Date(models.Model):
    date = models.DateField(null=True, blank=True)
    habit_status = models.PositiveIntegerField(null=True, blank=True)
    tracked_habits = models.ForeignKey("Habit", on_delete=models.SET_NULL, related_name='tracked_habit', null=True, blank=True)
    
    class Meta:
        constraints = [
            UniqueConstraint(fields=["tracked_habits", "date"], name="unique_user_date")
        ]
