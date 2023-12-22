from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.

def validate_due_date(value):
    today = timezone.now().date()

    if value < today:
        raise ValidationError("Due date must be on or after today.") 
    
class Task(models.Model):

    status_list = [
        ("todo", "todo"),
        ("active", "active"),
        ("done", "done")
    ]

    task_id = models.IntegerField(
        primary_key="True",
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    content = models.CharField(max_length=50)
    status = models.CharField(max_length=6, default="todo", choices=status_list)
    due = models.DateField(validators=[validate_due_date])
