from django import forms
from .models import Project

# Create your views here.
from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'goal', 'description', 'tutor', 'start_date', 'end_date']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Project title'})
        self.fields['goal'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Project goal'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Project description'})
        self.fields['tutor'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tutor'})
        self.fields['start_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_date'].widget.attrs.update({'class': 'form-control'})

        self.fields['title'].label = ''
        self.fields['goal'].label = ''
        self.fields['description'].label = ''
        self.fields['tutor'].label = ''
        self.fields['start_date'].label = ''
        self.fields['end_date'].label = ''


    def save(self, user, commit=True):
        team = user.team_assigned
        if not team:
            raise ValueError("No perteneces a un equipo.")

        if team.project_assigned:
            raise ValueError("Este equipo ya tiene un proyecto activo.")

        project = super().save(commit=False)
        project.created_by = user
        project.team_assigned = team
        if commit:
            project.save()
            team.project_assigned = project
            team.save()
        return project