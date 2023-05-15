from django.db import models
from django.contrib.auth.models import User
from workspaces.models import Workspace


class Board(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_post_mtcs8z',
        blank=True
    )

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f'{self.title}'
