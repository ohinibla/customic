import os
from pathlib import Path
from uuid import uuid4

from celery import states
from django.conf import settings
from django.db import models

# Create your models here.


def create_path(instance, filename):
    return os.path.join("mockups", str(instance.task.task_id), filename)


class TaskStatus(models.TextChoices):
    PENDING = states.PENDING
    SUCCESS = states.SUCCESS
    FAILED = states.FAILURE


class Colors(models.TextChoices):
    Blue = "0000FF"
    White = "FFFFFF"
    Yellow = "FFFF00"
    Black = "000000"


Fonts = models.TextChoices(
    "Fonts", list(f.stem for f in Path(settings.MEDIA_ROOT / "fonts").glob("*.ttf"))
)


Shirts = models.TextChoices(
    "Shirts", list(f.stem for f in Path(settings.MEDIA_ROOT / "pre").glob("*.png"))
)


class Task(models.Model):
    task_id = models.UUIDField(default=uuid4, unique=True)
    status = models.CharField(choices=TaskStatus)


class Mockup(models.Model):
    text = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to=create_path, blank=True, null=True)
    font = models.CharField(choices=Fonts, max_length=255, blank=True)
    text_color = models.CharField(
        choices=Colors, max_length=6, blank=True, default="FFFFFF"
    )
    shirt_color = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    task = models.ForeignKey(Task, related_name="mockups", on_delete=models.CASCADE)
