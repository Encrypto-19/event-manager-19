from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, TemplateView, UpdateView, DeleteView
from .forms import BoardCreateForm, TaskCreateForm
from .models import Board, Task
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.



class HomeView(TemplateView):
    template_name = 'scheduler/home.html'



class BoardCreateView(LoginRequiredMixin, CreateView):
    model = Board
    form_class = BoardCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskCreateView(LoginRequiredMixin, CreateView):
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


class BoardListView(LoginRequiredMixin, ListView):
    model = Board
    context_object_name = 'objects'


    def get_queryset(self):
        user = get_object_or_404(User, username = self.request.user.username)
        return Board.objects.filter(user = user)


# class BoardDetailView(DetailView):
#     model = Board


class BoardDetailView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = 'scheduler/board_detail.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        board = Board.objects.get(id = pk)
        tasks = Task.objects.filter(board = board)
        return render(request, self.template_name, {'board':board, 'tasks':tasks})

    def test_func(self):
        pk = self.kwargs.get('pk')
        print(pk)
        board = Board.objects.get(id = pk)
        if board.user == self.request.user:
            return True
        return False


class TaskDetailView(LoginRequiredMixin,UserPassesTestMixin, DetailView):
    model = Task

    def test_func(self):
        task = self.get_object()
        if task.board.user == self.request.user:
            return True
        return False


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = '/board/'

    def test_func(self):
        task = self.get_object()
        return task.board.user == self.request.user


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'end_date']

    def test_func(self):
        task = self.get_object()
        return task.board.user == self.request.user

class BoardUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Board
    fields = ['name']

    def test_func(self):
        board = self.get_object()
        return board.user == self.request.user



class BoardDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Board
    success_url = '/board/'

    def test_func(self):
        board = self.get_object()
        return board.user == self.request.user



