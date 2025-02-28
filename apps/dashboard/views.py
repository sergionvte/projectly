from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..projects.models import Project
from ..accounts.models import User, Team

# Create your views here.
@login_required(login_url='/login')
def dashboard(request):
    project = Project.objects.filter(
        created_by__email=request.user.email
    ).first()
    tasks = Task.objects.filter(
        assigned_to=request.user, completed=False
    )
    return render(
        request,
        'dashboard/dashboard.html',
        {
            'project': project,
            'tasks': tasks,
        }
    )

from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.task.models import Task
from apps.projects.models import Project
from apps.accounts.models import Team, User

@login_required
def tutor_dashboard(request, project_id):
    project = get_object_or_404(Project, id=project_id, tutor=request.user.email)
    team = project.team_assigned
    tasks = Task.objects.filter(project=project)
    members = team.members.all() if team else []

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "update_phase":
            new_phase = request.POST.get("project_phase")
            project.project_phase = new_phase
            project.save()
            messages.success(request, "Fase del proyecto actualizada.")

        elif action == "add_task":
            title = request.POST.get("title")
            description = request.POST.get("description")
            assigned_to_id = request.POST.get("assigned_to")
            assigned_to = User.objects.get(id=assigned_to_id) if assigned_to_id else None
            Task.objects.create(
                title=title,
                description=description,
                project=project,
                assigned_to=assigned_to.username if assigned_to else "No asignado",
                created_at=datetime.now(),
                due_date=request.POST.get("due_date"),
                status="Pendiente"
            )
            messages.success(request, "Tarea creada correctamente.")

        elif action == "delete_task":
            task_id = request.POST.get("task_id")
            Task.objects.filter(id=task_id).delete()
            messages.success(request, "Tarea eliminada.")

        return redirect("tutor_dashboard", project_id=project.id)

    return render(request, "tutor_dashboard.html", {
        "project": project,
        "tasks": tasks,
        "members": members,
    })