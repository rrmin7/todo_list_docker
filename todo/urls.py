from django.urls import path
from .views import TaskListView, TaskDetailView, TaskUpdateView, TaskCreateView, complete_task

app_name = "todo"

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("task/create/", TaskCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/complete/", complete_task, name="complete_task"),  ]

