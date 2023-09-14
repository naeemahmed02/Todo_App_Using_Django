from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task


# Home Function
def index(request):
    # Get all tasks from the database
    tasks = Task.objects.all()

    # Check if a new task is submitted via a POST request
    if request.method == 'POST':
        task_title = request.POST['task']
        # Create a new task with the submitted title
        Task.objects.create(title=task_title)

    # Prepare the context with the list of tasks
    context = {'tasks': tasks}

    # Render the 'index.html' template with the context
    return render(request, 'Task/index.html', context)


def update_item(request, pk):
    # Get the task with the specified primary key (pk)
    task = Task.objects.get(id=pk)

    # Check if the form for updating the task is submitted via POST
    if request.method == 'POST':
        # Update the task's title with the submitted value
        task.title = request.POST['title']
        task.save()
        # Redirect back to the 'index' page after updating
        return redirect('index')

    # Render the 'update_task.html' template with the task data
    return render(request, 'Task/update_task.html', {'task': task})


def delete_item(request, pk):
    # Get the task with the specified primary key (pk)
    item = Task.objects.get(id=pk)

    # Check if the delete form is submitted via POST
    if request.method == 'POST':
        # Delete the task from the database
        item.delete()
        # Redirect back to the 'index' page after deletion
        return redirect('index')

    # Render the 'delete_task.html' template with the task data
    return render(request, 'Task/delete_task.html', {'item': item})


def finished(request, pk):
    # Get the task with the specified primary key (pk)
    task = Task.objects.get(id=pk)

    # Mark the task as complete
    task.completed = True
    task.save()

    # Redirect back to the 'index' page after marking as complete
    return redirect('index')
