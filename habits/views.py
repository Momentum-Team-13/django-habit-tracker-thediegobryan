from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Habit, Date, User
from .forms import HabitForm, DateForm
# Create your views here.

def homepage(request):
    if request.user.is_authenticated:
        return redirect("list_habits")
    return render(request, "habits/homepage.html")

def list_habits(request):
    habits = Habit.objects.all()
    return render(request, "habits/list_habits.html", {"habits": habits})

def new_habit(request):
    if request.method == 'GET':
        form = HabitForm()
    else:
        form = HabitForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_habits')
    
    return render(request, "habits/new_habit.html", {"form":form})

def status(request):
    if request.method == 'GET':
        form = DateForm()
    else:
        form = DateForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_habits')
    
    return render(request, "habits/status.html", {"form":form})