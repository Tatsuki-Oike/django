from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def index(request):

    data = Task.objects.all()

    params = {
        "data": data,
    }

    return render(request, "crud_app/index.html", params)

def delete_all(request):

    if request.method == "POST":
        Task.objects.all().delete()

    return redirect(to="/crud")

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

def delete(request, id):
    
    if request.method == "POST":
        Task.objects.get(task_id = id).delete()

    return redirect(to="/crud")