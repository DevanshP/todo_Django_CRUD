

from django.shortcuts import render
from todoapp.models import Task

def home(request):
    tasks = Task.objects.filter(isComplted=False).order_by('-updated_at')
    context = {
        'tasks': tasks,
    }
    return render(request,'home.html',context)


