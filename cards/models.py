from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from lists.models import List


class Card(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    priority_color = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    due_time = models.DateTimeField(null=True)
    members = models.ManyToManyField(
        User,
        related_name='member_models',
        blank=True)
    file = models.FileField(
        upload_to='uploads/',
        blank=True,
        null=True,
        storage=RawMediaCloudinaryStorage())

    class Meta:
        ordering = ['id']
        # unique_together=      **Discover how to use properly

    def __str__(self):
        return f'{self.title}'
