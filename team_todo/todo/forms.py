from django import forms
from .models import Board, Task, TaskComment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name', 'description', 'is_public']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'image', 'status']

class CommentForm(forms.ModelForm):
    class Meta:
        model = TaskComment
        fields = ['text']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']