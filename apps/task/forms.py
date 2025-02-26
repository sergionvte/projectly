from django import forms
from apps.accounts.models import User, Team
from .models import Task, Comment, Evidence

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'rows': 3}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'assigned_to': forms.Select(attrs={'class': 'form-control', 'rows': 3}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'rows': 3, 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user and hasattr(user, 'team_assigned') and user.team_assigned:
            self.fields['assigned_to'].queryset = user.team_assigned.members.all()
        else:
            self.fields['assigned_to'].queryset = User.objects.none()


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