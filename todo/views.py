from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_text', 'due_date', 'is_important']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class TaskListView(ListView):
    model = Task
    template_name = "todo/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(due_date__gte=timezone.now()).order_by('due_date')

class TaskDetailView(DetailView):
    model = Task
    template_name = "todo/task_detail.html"
    context_object_name = "task"

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = "/todo/"

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = "/todo/"

def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.delete()
    return redirect("todo:task_list")

