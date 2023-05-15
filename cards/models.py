from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    list = models.IntegerField()
    content = models.TextField(max_length=1000)
    priority_color = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    due_time = models.DateTimeField()
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(
        upload_to='uploads/',
        blank=True
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.title}'
