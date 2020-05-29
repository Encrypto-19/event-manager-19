
from django import forms
from django.contrib.auth.models import User
from .models import Board, Task


class BoardCreateForm(forms.ModelForm):

    class Meta:
        model = Board
        fields =['name']

class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'end_date']