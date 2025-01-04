from django import forms
from .models import Project

# Create your views here.
class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'description',
            'tutor',
            'start_date',
            'end_date',
            'project_url',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'tutor': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.TextInput(attrs={'class': 'form-control', 'type':'datetime-local'}),
            'end_date': forms.TextInput(attrs={'class': 'form-control', 'type':'datetime-local'}),
            'project_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

