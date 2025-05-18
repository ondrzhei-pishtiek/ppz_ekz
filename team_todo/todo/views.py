from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Task, TaskComment
from .forms import BoardForm, TaskForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegisterForm

@login_required
def home(request):
    boards = Board.objects.filter(owner=request.user) | Board.objects.filter(is_public=True)
    return render(request, 'todo/home.html', {'boards': boards})

@login_required
def board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.owner = request.user
            board.save()
            return redirect('home')
    else:
        form = BoardForm()
    return render(request, 'todo/board_form.html', {'form': form})

@login_required
def task_create(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.board = board
            task.created_by = request.user
            task.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'todo/task_form.html', {'form': form, 'board': board})

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    comments = task.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.author = request.user
            comment.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = CommentForm()
    return render(request, 'todo/task_detail.html', {'task': task, 'comments': comments, 'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # автоматичний логін після реєстрації
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'todo/register.html', {'form': form})