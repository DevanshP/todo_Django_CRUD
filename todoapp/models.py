from django.db import models

# Create your models here. \\\\


# two feild taks name and task status completed or not completed


class Task(models.Model):
    task = models.CharField(max_length=250)
    isComplted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.task


