from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["task_id", "content", "status", "due"]
        widgets = {
            'task_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'due': forms.DateInput(attrs={"class": "form-control"})
        }
