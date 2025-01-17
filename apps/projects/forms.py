from django import forms
from .models import Project

# Create your views here.
class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'description',
            'goal',
            'tutor',
            'start_date',
            'end_date',
            'project_url',
            'project_tiktok',
            'project_instagram',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'goal': forms.TextInput(attrs={'class': 'form-control'}),
            'tutor': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.TextInput(attrs={'class': 'form-control', 'type':'date'}),
            'end_date': forms.TextInput(attrs={'class': 'form-control', 'type':'date'}),
            'project_url': forms.TextInput(attrs={'class': 'form-control'}),
            'project_tiktok': forms.TextInput(attrs={'class': 'form-control'}),
            'project_instagram': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)


class ProjectJoinTeamForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['team_assigned']
        widgets = {
            'team_assigned': forms.TextInput(attrs={'class': 'form-control'}),
        }