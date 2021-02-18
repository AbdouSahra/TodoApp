from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskForm


class TaskListView(ListView):
    model = Task
    template_name = 'task/home.html'
    context_object_name = 'tasks'
    ordering = '-date_created'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task/create.html'
    form_class = TaskForm
    success_url = '/'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task/create.html'
    form_class = TaskForm
    success_url = '/'


class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/'

    def get(self, request, *arg, **kwargs):
        return self.post(request, *arg, **kwargs)
