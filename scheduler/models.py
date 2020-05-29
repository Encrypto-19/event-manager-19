from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('board-list')


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + self.board.name

    def get_absolute_url(self):
        return reverse('board-list')
