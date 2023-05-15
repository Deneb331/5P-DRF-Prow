from django.db import models
from django.contrib.auth.models import User
from boards.models import Board


class List(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title}"
