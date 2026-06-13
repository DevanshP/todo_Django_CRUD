from django.urls import path
from . import views

urlpatterns = [
    path('addTask/',views.addTask,name='addTask'),
    path('completeTask/<int:pk>/',views.completeTask,name='completeTask'),
    path('markAsUnDone/<int:pk>/',views.markAsUnDone,name='markAsUnDone'),
]






