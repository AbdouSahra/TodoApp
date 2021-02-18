
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'complete']
        labels = {'name': 'Name'}
        widgets = {
            'name': forms.TextInput(attrs={'classes': 'form-control', 'placeholder':'Add new task...'})
        }
