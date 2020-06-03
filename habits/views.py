from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Habit

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect(to='list_habits')

    return render(request, "habits/index.html",)

@login_required
def list_habits(request):
    habits = request.user.habits.all()
    return render(request, "habits/list_habits.html", {"habits": habits})

@login_required
def habit_detail(request, habit_pk):
    habit = get_object_or_404(request.user.habits, pk=habit_pk)
    return render(request, "habits/habit_detail.html", {"habit": habit})
