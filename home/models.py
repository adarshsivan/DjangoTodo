from django.db import models

# Create your models here.
class ToDo(models.Model):
    TaskName = models.CharField(max_length=300)
    Description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.TaskName