from django.db import models

class Task(models.Model):
    task_text = models.CharField(max_length=200)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    is_important = models.BooleanField(default=False)
    

    def __str__(self):
        return self.task_text

