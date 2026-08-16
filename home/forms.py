from django import forms
from .models import ToDoModel


class TodoForm(forms.ModelForm):
    class Meta:
        model = ToDoModel
        fields = '__all__'
