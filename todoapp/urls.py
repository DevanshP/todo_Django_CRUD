from django.urls import path
from . import views

urlpatterns = [
    #add task feature
    path('addTask/',views.addTask,name='addTask'),

    #mark as done url pattern 
    path('completeTask/<int:pk>/',views.completeTask,name='completeTask'),

    # makr as undone feature 
    path('markAsUnDone/<int:pk>/',views.markAsUnDone,name='markAsUnDone'),

    #Edit Task Feature 
    path('edit_task/<int:pk>/',views.edit_task,name='edit_task'),

    # Delete URL pattern to delete the task 
    path('delete_task/<int:pk>/',views.delete_task,name='delete_task'),

     
]






