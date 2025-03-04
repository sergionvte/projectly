from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Project

@login_required
def create_project(request):
    team = request.user.team_assigned

    if not team or team.created_by != request.user:
        return redirect('dashboard')

    if team.project_assigned:
        return redirect('dashboard')

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
    project = get_object_or_404(Project, id=project_id)

    return render(request, 'projects/project_detail.html', {'project': project})


def project_edit(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if project.created_by != request.user:
        return redirect('project_detail', project_id=project.id)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectForm(instance=project)

    return render(request, 'projects/project_edit.html', {'form': form, 'project': project})


# API de verificacion
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .services import find_similar_projects

@csrf_exempt
def check_project_similarity(request):
    """Verifica si un proyecto tiene similitud con otro en la BD."""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            title = data.get("title", "")
            description = data.get("description", "")

            if not title or not description:
                return JsonResponse({"error": "Se requieren título y descripción."}, status=400)

            similar_projects = find_similar_projects(title, description, threshold=0.8)

            return JsonResponse({"similar_projects": similar_projects})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Método no permitido"}, status=405)