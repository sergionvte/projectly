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


from django.shortcuts import render, get_object_or_404
from .models import Project

def project_detail(request, project_id):
    # Obtener el proyecto según el ID
    project = get_object_or_404(Project, id=project_id)

    # Renderizar el template con el proyecto
    return render(request, 'projects/project_detail.html', {'project': project})


def project_edit(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if project.created_by != request.user:
        # Redirigir si el usuario no es el creador
        return redirect('project_detail', project_id=project.id)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectForm(instance=project)

    return render(request, 'projects/project_edit.html', {'form': form, 'project': project})
