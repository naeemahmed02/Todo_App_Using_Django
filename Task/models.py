from django.db import models


# Create your models here.

class Task(models.Model):
    # Define a field for the task title with a maximum length of 200 characters
    title = models.CharField(max_length=200)

    # Define a field to track whether the task is complete (default to False)
    complete = models.BooleanField(default=False)

    # Define a field to automatically record the creation date and time
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Return the task title as the string representation of the task
        return self.title
