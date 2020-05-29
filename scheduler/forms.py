
from django import forms
from django.contrib.auth.models import User
from .models import Board, Task


class DateInput(forms.DateInput):
    input_type = 'date'



class BoardCreateForm(forms.ModelForm):

    class Meta:
        model = Board
        fields =['name']

class TaskCreateForm(forms.ModelForm):
    end_date = forms.DateTimeField(widget=DateInput)
    class Meta:
        model = Task
        fields = ['title', 'description', 'end_date']