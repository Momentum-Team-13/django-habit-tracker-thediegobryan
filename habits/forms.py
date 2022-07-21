from django import forms
from .models import Habit, Date

class DateInput(forms.DateInput):
    input_type = 'date'

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'habit_name',
            'goal',
            'metric',
        ]

class DateForm(forms.ModelForm):
    class Meta:
        model = Date
        fields = [
            'date',
            'tracked_habit',
            'habit_status',
        ]
        widgets = {
            'date': DateInput(),
        }