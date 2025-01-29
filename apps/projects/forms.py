from django import forms
from .models import Project

# Create your views here.
from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'goal', 'description', 'tutor', 'start_date', 'end_date']

    def save(self, user, commit=True):
        team = user.team_assigned  # Obtiene el equipo del usuario
        if not team:
            raise ValueError("No perteneces a un equipo.")

        if team.project_assigned:
            raise ValueError("Este equipo ya tiene un proyecto activo.")

        project = super().save(commit=False)
        project.created_by = user
        project.team_assigned = team
        if commit:
            project.save()
            team.project_assigned = project  # Asigna el proyecto al equipo
            team.save()
        return project
