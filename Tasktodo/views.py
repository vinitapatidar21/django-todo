from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm
from .models import Todo

def index(request):
    item_list = Todo.objects.order_by("-date")  # List of todo items

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task added!")
            return redirect('todo')  # Make sure 'todo' is your correct URL name
    else:
        form = TodoForm()

    context = {
        "forms": TodoForm,             
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'Tasktodo/index.html', context)

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Task removed!")
    return redirect('todo')  # Make sure this name matches your urls.py
