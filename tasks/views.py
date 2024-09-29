# tasks/views.py
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Task, Category
from django.views.generic.edit import CreateView
from .forms import TaskForm

class Task_List_View(ListView):
    model = Task
    template_name = 'tasks/task_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')
        search_query = self.request.GET.get('search')

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        return queryset

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'

