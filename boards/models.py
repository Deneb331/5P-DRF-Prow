from django.db import models
from django.contrib.auth.models import User
from workspaces.models import Workspace


class Board(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE)
    title = models.CharField(max_length=255, blank=False)
    workspace = models.ForeignKey(Workspace, on_delete=CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_post_mtcs8z',
        blank=True
    )
