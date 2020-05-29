from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, TemplateView, UpdateView, DeleteView
from .forms import BoardCreateForm, TaskCreateForm
from .models import Board, Task
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
# Create your views here.



class HomeView(TemplateView):
    template_name = 'scheduler/home.html'



class BoardCreateView(CreateView):
    model = Board
    form_class = BoardCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            print('forms valid')
            task = form.save(commit=False)
            task.board = Board.objects.get(id = pk)
            form.save()
            return redirect('board-list')
        print('form invalid')
        return render(request, 'scheduler/task_form.html', {'form':form})


class BoardListView(ListView):
    model = Board
    context_object_name = 'objects'


    def get_queryset(self):
        user = get_object_or_404(User, username = self.request.user.username)
        return Board.objects.filter(user = user)

# class BoardDetailView(DetailView):
#     model = Board


class BoardDetailView(View):
    template_name = 'scheduler/board_detail.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        print(pk)
        board = Board.objects.get(id = pk)
        tasks = Task.objects.filter(board = board)
        return render(request, self.template_name, {'board':board, 'tasks':tasks})


class TaskDetailView(DetailView):
    model = Task


class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/board/'


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'end_date']

class BoardUpdateView(UpdateView):
    model = Board
    fields = ['name']


class BoardDeleteView(DeleteView):
    model = Board
    success_url = '/board/'



