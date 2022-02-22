from email.policy import default
from statistics import mode
from django.db import models
import uuid
# Create your models here.

class Project(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=25, blank=True, null=True)
    project_image = models.ImageField(null=True, blank=True, default="default-project.jpg", upload_to="images/projects")
    short_intro = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title