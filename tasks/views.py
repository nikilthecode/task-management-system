from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


@login_required
def home(request):

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("/")

    form = TaskForm()
    tasks = Task.objects.filter(user=request.user)
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = tasks.filter(completed=False).count()

    return render(request, "home.html", {
    "tasks": tasks,
    "form": form,
    "completed_tasks": completed_tasks,
    "pending_tasks": pending_tasks,
})
@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("/")

    form = TaskForm(instance=task)

    return render(request, "edit.html", {
        "form": form
    })
@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == "POST":
        task.delete()
        return redirect("/")

    return render(request, "delete.html", {
        "task": task
    })
@login_required
def toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    task.completed = not task.completed
    task.save()

    return redirect("/")