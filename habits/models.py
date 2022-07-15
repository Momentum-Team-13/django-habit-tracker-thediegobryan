from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_date(date):
    if date >= timezone.now().date():
        raise ValidationError("Date cannot be in the future")

# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return self.username

class Habit(models.Model):
    habit_name = models.CharField(max_length=255)
    goal = models.PositiveIntegerField()
    metric = models.CharField(max_length=255)
    creator = models.ForeignKey("User", on_delete=models.SET_NULL, related_name='habits', null=True, blank=True)

class Date(models.Model):
    date = models.DateField(default=None, validators=[validate_date])
    habit_status = models.PositiveIntegerField()
    tracked_habit = models.ForeignKey("Habit", on_delete=models.CASCADE, related_name='dates')
    
    class Meta:
        constraints = [
            UniqueConstraint(fields=["tracked_habit", "date"], name="unique_user_date")
        ]