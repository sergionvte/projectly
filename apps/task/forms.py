from django import forms
from .models import Task, Comment, Evidence

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'due_date']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class EvidenceForm(forms.ModelForm):
    class Meta:
        model = Evidence
        fields = ['file']