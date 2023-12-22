# models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_due_date(value):
    if value < timezone.now().date():
        raise ValidationError("Due date must be in the future.")

class Task(models.Model):
    status_list = [
        ("todo", "todo"),
        ("active", "active"),
        ("done", "done")
    ]

    task_id = models.IntegerField(
        primary_key=True,
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    content = models.CharField(max_length=50)
    status = models.CharField(max_length=6, default="todo", choices=status_list)
    due = models.DateField(validators=[validate_due_date])
