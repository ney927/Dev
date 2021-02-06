from django import forms
from .models import Tasks

class createTask(forms.ModelForm):
  class Meta:
    model = Tasks
    fields = [
      'item',
      'completed',
    ]