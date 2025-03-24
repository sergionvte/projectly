from django import forms
from .models import Project
from .services import get_embedding

class ProjectForm(forms.ModelForm):
    project_phase = forms.ChoiceField(
        choices=Project.PHASE_CHOICES.items(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Fase del Proyecto"
    )

    class Meta:
        model = Project
        fields = ['title', 'goal', 'description', 'tutor', 'start_date', 'end_date', 'project_phase', 'project_url', 'project_tiktok', 'project_instagram']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'goal': forms.Textarea(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'tutor': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'project_url': forms.TextInput(attrs={'class': 'form-control'}),
            'project_tiktok': forms.TextInput(attrs={'class': 'form-control'}),
            'project_instagram': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Título del proyecto'
        self.fields['goal'].label = 'Objetivo del proyecto'
        self.fields['description'].label = 'Descripción del proyecto'
        self.fields['tutor'].label = 'Manager del proyecto'
        self.fields['start_date'].label = 'Fecha de inicio'
        self.fields['end_date'].label = 'Fecha de finalización'
        self.fields['project_phase'].label = 'Fase del proyecto'

    def save(self, user, commit=True):
        team = user.team_assigned
        if not team:
            raise ValueError("No perteneces a un equipo.")

        # Solo validar si es un nuevo proyecto
        if not self.instance.pk and team.project_assigned:
            raise ValueError("Este equipo ya tiene un proyecto activo.")

        project = super().save(commit=False)
        project.created_by = user
        project.team_assigned = team

        text = f"{self.cleaned_data['title']} {self.cleaned_data['description']}"
        project.embedding = get_embedding(text)

        if commit:
            project.save()  # Guardamos el proyecto

            # Solo asignar el proyecto si es nuevo
            if not self.instance.pk:
                team.project_assigned = project
                team.save()

        return project