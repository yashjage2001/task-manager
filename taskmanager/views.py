from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from .models import Task
from .forms import createform 
from django.urls import reverse_lazy


# Create your views here.
class tasklist(ListView):
    model=Task
    template_name='showtask.html'
    context_object_name='to'

class createtask(CreateView):
    model=Task
    form_class=createform
    template_name="createtask.html"
    success_url=reverse_lazy('tasklist')


class updatetask(UpdateView):
    model=Task
    form_class=createform
    template_name='updatetask.html'
    success_url=reverse_lazy('tasklist')

class detailtask(DetailView):
    model=Task
    template_name='taskdetail.html'
    context_object_name='i'

class deletetask(DeleteView):
    model=Task
    template_name='deletetask.html'
    success_url=reverse_lazy('tasklist')
