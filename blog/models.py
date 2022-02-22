from statistics import mode
from tkinter.tix import Tree
from uuid import UUID
from django.db import models
import uuid

# Create your models here.

class Blog(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title