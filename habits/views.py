from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Habit, Date, User
from .forms import HabitForm, DateForm
# Create your views here.

def homepage(request):
    if request.user.is_authenticated:
        return redirect("list_habits")
    return render(request, "habits/homepage.html")

@login_required
def list_habits(request):
    habits = Habit.objects.filter(creator=request.user)
    user = request.user
    dates = Date.objects.filter(tracked_habit__creator=request.user).order_by('-date')
    return render(request, "habits/list_habits.html", {"habits":habits, "user":user, "dates":dates})

@login_required
def new_habit(request):
    if request.method == 'GET':
        form = HabitForm()
    else:
        form = HabitForm(data = request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.creator = request.user
            form.save()
            return redirect(to='list_habits')
    
    return render(request, "habits/new_habit.html", {"form":form})

@login_required
def status(request):
    habits = Habit.objects.filter(creator=request.user)
    if request.method == 'GET':
        form = DateForm()
        form.fields["tracked_habit"].queryset=habits
    else:
        form = DateForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_habits')
    
    return render(request, "habits/status.html", {"form":form})

@login_required
def status_detail(request,pk, year, month, day):
    status = get_object_or_404(Date, pk=pk)
    status_entries = Date.objects.filter(date=status.date, tracked_habit__creator=request.user)
    year = status.date.year
    month = status.date.month
    day = status.date.day
    return render(request, "habits/status_detail.html", {
        "status": status, 
        "year":year,
        "month":month, 
        "day":day, 
        "status_entries":status_entries
        }
        )

@login_required
def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habit_entries = Date.objects.filter(tracked_habit__creator=request.user, tracked_habit__habit_name=habit.habit_name)
    return render(request, "habits/habit_detail.html",{"habit":habit, "habit_entries":habit_entries})
    