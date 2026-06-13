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

def edit_task(request,pk):
    get_task = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
        
    else:
        context = {
            'get_task' : get_task,
        }

        return render(request,'edit_task.html',context)
    
def delete_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete() #delete is in inbulit object used to delete the object 
    return redirect('home')


