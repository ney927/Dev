from django.shortcuts import render, redirect
from .models import Tasks
from .forms import createTask

# Create your views here.

def tasks_list_view(request):
  queryset = Tasks.objects.all()
  context={
    'obj_list': queryset
  }
  return render(request, 'ToDo/tasks_list.html', context)

def tasks_create_view(request):
  form = createTask(request.POST)
  if form.is_valid():
    form.save()
    return redirect('tasks-list')
  context = {
    'form': form
  }
  return render(request,'ToDo/tasks_create.html', context)

def tasks_delete_view(request, id):
  object = Tasks.objects.get(id=id)
  object.delete()
  return redirect('tasks-list')
  queryset = Tasks.objects.all()
  context={
    'obj_list': queryset
  }
  return render(request, 'ToDo/tasks_list.html', context)

def tasks_complete_view(request, id):
  object = Tasks.objects.get(id=id)
  object.completed = not object.completed
  object.save()
  return redirect('tasks-list')
  queryset = Tasks.objects.all()
  context={
    'obj_list': queryset
  }
  return render(request, 'ToDo/tasks_list.html', context)
