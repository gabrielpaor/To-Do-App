from django import forms
from django.forms import ModelForm

from .models import *

#specify which model and task is included in a form
class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter new task...'}))

    class Meta:
        model = Task
        fields = '__all__'