from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Task, Comment, Evidence
from .forms import TaskForm, CommentForm, EvidenceForm

@login_required
def task_list(request):
    team = request.user.team_assigned
    tasks = Task.objects.filter(team=team)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if not task.can_user_access(request.user):
        return HttpResponseForbidden("No tienes acceso a esta tarea.")

    comments = task.comments.all()
    evidence = task.evidences.all()
    comment_form = CommentForm()
    evidence_form = EvidenceForm()
    return render(request, 'tasks/task_detail.html', {
        'task': task,
        'comments': comments,
        'evidence': evidence,
        'comment_form': comment_form,
        'evidence_form': evidence_form
    })

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.team = request.user.team_assigned
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def add_comment(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if not task.can_user_access(request.user):
        return HttpResponseForbidden("No tienes acceso a esta tarea.")

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.user = request.user
            comment.save()
    return redirect('task_detail', task_id=task.id)

@login_required
def upload_evidence(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if not task.can_user_access(request.user):
        return HttpResponseForbidden("No tienes acceso a esta tarea.")

    if request.method == 'POST':
        form = EvidenceForm(request.POST, request.FILES)
        if form.is_valid():
            evidence = form.save(commit=False)
            evidence.task = task
            evidence.uploaded_by = request.use
            evidence.save()
    return redirect('task_detail', task_id=task.id)

@login_required
def mark_task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if not task.can_user_access(request.user):
        return HttpResponseForbidden("No tienes acceso a esta tarea.")

    task.completed = True
    task.save()
    return redirect('task_detail', task_id=task.id)