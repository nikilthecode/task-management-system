from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def home(request):

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")

    form = TaskForm()
    tasks = Task.objects.all()

    return render(request, "home.html", {
        "tasks": tasks,
        "form": form
    })
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("/")

    form = TaskForm(instance=task)

    return render(request, "edit.html", {
        "form": form
    })
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.delete()
        return redirect("/")

    return render(request, "delete.html", {
        "task": task
    })