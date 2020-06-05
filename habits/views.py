from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import HabitForm, RecordForm

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect(to='list_habits')

    return render(request, "habits/index.html",)

@login_required
def list_habits(request):
    your_habits = request.user.habits.all()
    return render(request, "habits/list_habits.html", {"habits": your_habits})

@login_required
def show_habit(request, habit_pk):
    habit = get_object_or_404(request.user.habits, pk=habit_pk)
    return render(request, "habits/show_habit.html", {"habit": habit})

@login_required
def add_habit(request):
    if request.method == "POST":
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect(to='list_habits')
    else:
        form = HabitForm()

    return render(request, "habits/add_habit.html", {"form": form})

@login_required
def delete_habit(request, habit_pk):
    habit = get_object_or_404(request.user.habits, pk=habit_pk)
    if request.method == 'POST':
        habit.delete()
        return redirect(to='list_habits')

    return render(request, "delete_habit.html", {"habit": habit})

@login_required
def add_record(request, habit_pk):
    habit = get_object_or_404(request.user.habits, pk=habit_pk)

    if request.method == "POST":
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.habit = habit
            record.save()
            return redirect(to='show_habit', habit_pk=habit.pk)
    else:
        form = RecordForm()

    return render(request, "habits/add_record.html", {"form": form, "habit": habit})