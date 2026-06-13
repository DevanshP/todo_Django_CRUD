from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

# Create your views here.



def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')


def completeTask(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.isComplted = True
    task.save()
    return redirect('home')

def markAsUnDone(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.isComplted = False
    task.save()
    return redirect('home')

