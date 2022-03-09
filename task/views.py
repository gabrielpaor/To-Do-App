from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

from .models import *

def index(request):
    task = Task.objects.all()

#TaskForm is a class inside .forms
    form = TaskForm()

#If the user click submit, then save it and redirect to the same page.
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


    context = {'task':task, 'form':form}
    return render(request, 'task/list.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'task/update_task.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'task/delete_task.html', context)

