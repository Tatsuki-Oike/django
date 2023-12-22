from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Task
from .forms import TaskForm

# Create your views here.

def custom_logout(request):
    logout(request)
    return redirect(to="/user")

@login_required(login_url="/user/login/")
def index(request):

    task = TaskForm()
    data = Task.objects.all()

    params = {
        "user": request.user,
        "data": data,
        "form": task
    }

    return render(request, "crud_app/index.html", params)


@login_required(login_url="/user/login/")
def create(request):

    if request.method == "POST":
        try:
            task = Task()
            task = TaskForm(request.POST, instance=task)
            task.save()
            return redirect(to="/crud")
        except Exception as e:
            msg = f"データの更新に失敗しました。{e}"
    else:
        msg = "データを作成"
        task = TaskForm()

    params = {
        "msg": msg,
        "form": task
    }

    return render(request, "crud_app/create.html", params)


@login_required(login_url="/user/login/")
def delete_all(request):

    if request.method == "POST":
        Task.objects.all().delete()

    return redirect(to="/crud")


@login_required(login_url="/user/login/")
def update(request, id):

    item = Task.objects.get(task_id = id)
    if request.method == "POST":
        try:
            task = TaskForm(request.POST, instance=item)
            task.save()
            return redirect(to="/crud")
        except Exception as e:
            msg = "データの更新に失敗しました。"
    else:
        msg = "データの更新"
    
    params = {
        "msg": msg,
        "id": id,
        "form": TaskForm(instance=item)
    }

    return render(request, "crud_app/update.html", params)


@login_required(login_url="/user/login/")
def delete(request, id):
    
    if request.method == "POST":
        Task.objects.get(task_id = id).delete()

    return redirect(to="/crud")