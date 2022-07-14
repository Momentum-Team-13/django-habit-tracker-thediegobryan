from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Habit, Date, User
# Create your views here.

def homepage(request):
    if request.user.is_authenticated:
        return redirect("list_habits")
    return render(request, "habits/homepage.html")

def list_habits(request):
    habits = Habit.objects.all()
    return render(request, "habits/list_habits.html", {"habits": habits})