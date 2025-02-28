from django import forms
from apps.accounts.models import User, Team
from .models import Task, Comment, Evidence
from django.core.exceptions import ValidationError


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'assigned_to': forms.Select(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user and self.user.team_assigned:
            self.fields['assigned_to'].queryset = self.user.team_assigned.members.all()

    def clean_title(self):
        title = self.cleaned_data.get('title')
        team = self.user.team_assigned  # Obtener el equipo del usuario

        if Task.objects.filter(title=title, team=team).exists():
            raise ValidationError("Ya existe una tarea con este título en tu equipo.")

        return title


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class EvidenceForm(forms.ModelForm):
    class Meta:
        model = Evidence
        fields = ['file']
        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control', 'rows': 3, 'type': 'file'}),
        }