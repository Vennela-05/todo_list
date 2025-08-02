# from django.shortcuts import render, redirect
# from .models import Task
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User

# def register_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         if not User.objects.filter(username=username).exists():
#             User.objects.create_user(username=username, password=password)
#             return redirect('login')
#     return render(request, 'register.html')

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('index')
#     return render(request, 'login.html')

# def logout_view(request):
#     logout(request)
#     return redirect('login')

# @login_required
# def index(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         if title:
#             Task.objects.create(user=request.user, title=title)
#         return redirect('index')

#     tasks = Task.objects.filter(user=request.user).order_by('-created_at')
#     return render(request, 'index.html', {'tasks': tasks})

# @login_required
# def complete_task(request, task_id):
#     task = Task.objects.get(id=task_id, user=request.user)
#     task.completed = True
#     task.save()
#     return redirect('index')

# @login_required
# def delete_task(request, task_id):
#     task = Task.objects.get(id=task_id, user=request.user)
#     task.delete()
#     return redirect('index')

# from django.shortcuts import redirect, get_object_or_404
# from .models import Task

# def uncomplete_task(request, task_id):
#     task = get_object_or_404(Task, id=task_id)
#     task.completed = False
#     task.save()
#     return redirect('index')
# from django.shortcuts import redirect, get_object_or_404
# from .models import Task

# def complete_task(request, task_id):
#     task = get_object_or_404(Task, id=task_id)
#     task.completed = not task.completed  # Toggle completion
#     task.save()
#     return redirect('index')



from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password=password)
            return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')  # Include due date
        category = request.POST.get('category')  # Include category
        if title:
            Task.objects.create(user=request.user, title=title, due_date=due_date, category=category)
        return redirect('index')

    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'index.html', {'tasks': tasks})

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed  # Toggle completion
    task.save()
    return redirect('index')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('index')
