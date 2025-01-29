from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Project

@login_required
def create_project(request):
    team = request.user.team_assigned

    if not team or team.created_by != request.user:
        return redirect('dashboard')  # Solo el creador del equipo puede crear un proyecto

    if team.project_assigned:
        return redirect('dashboard')  # Evita que un equipo tenga más de un proyecto

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            return redirect('dashboard')
    else:
        form = ProjectForm()

    return render(request, 'projects/create_project.html', {'form': form})
