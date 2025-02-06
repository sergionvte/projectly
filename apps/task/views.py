from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task, Evidence
from .forms import TaskForm, EvidenceForm
from apps.accounts.models import User, Team

# Vista para que el tutor asigne tareas
@login_required
def create_task(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    # Verificar que el usuario es tutor
    if not request.user.is_tutor:
        messages.error(request, "No tienes permisos para asignar tareas.")
        return redirect("dashboard")

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.team = team
            task.save()
            messages.success(request, "Tarea asignada exitosamente.")
            return redirect("team_detail", team_id=team.id)
    else:
        form = TaskForm()

    return render(request, "tasks/create_task.html", {"form": form, "team": team})

# Vista para que los estudiantes vean sus tareas
@login_required
def student_tasks(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, "tasks/student_tasks.html", {"tasks": tasks})

# Marcar tarea como completada
@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    # Solo el estudiante asignado puede completar su tarea
    if request.user != task.assigned_to:
        messages.error(request, "No puedes marcar esta tarea como completada.")
        return redirect("student_tasks")

    task.completed = True
    task.save()
    messages.success(request, "Tarea completada exitosamente.")
    return redirect("student_tasks")

# Subir evidencia
@login_required
def upload_evidence(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.user != task.assigned_to:
        messages.error(request, "No puedes subir evidencia para esta tarea.")
        return redirect("student_tasks")

    if request.method == "POST":
        form = EvidenceForm(request.POST, request.FILES)
        if form.is_valid():
            evidence = form.save(commit=False)
            evidence.task = task
            evidence.uploaded_by = request.user
            evidence.save()
            messages.success(request, "Evidencia subida exitosamente.")
            return redirect("student_tasks")
    else:
        form = EvidenceForm()

    return render(request, "tasks/upload_evidence.html", {"form": form, "task": task})
