

from django.shortcuts import render
from todoapp.models import Task

def home(request):
    tasks = Task.objects.filter(isComplted=False).order_by('-updated_at')
    completed_task = Task.objects.filter(isComplted=True)
    markAsUnDone = Task.objects.filter(isComplted=False)

    context = {
        'tasks': tasks,
        'completed_task': completed_task,
        'markAsUnDone': markAsUnDone,

    }
    return render(request,'home.html',context)


