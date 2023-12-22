from django.shortcuts import render, redirect
from .models import Task, NewTask
from .forms import TaskForm, NewTaskForm

# Create your views here.

def index(request):

    if request.method == "POST":
        task = Task()
        task.task_id = request.POST["task_id"]
        task.content = request.POST["content"]
        task.save()
        msg = "データを登録しました"
    else:
        msg = "データを登録してください"

    data = Task.objects.all()
    params = {
        "data": data,
        "msg": msg
    }
    return render(request, "model_app/01_index.html", params)


def form(request):

    if request.method == "POST":
        task = Task()
        task = TaskForm(request.POST, instance=task)
        task.save()
        msg = "データを登録しました"
    else:
        msg = "データを登録してください"

    data = Task.objects.all()
    params = {
        "data": data,
        "msg": msg,
        "form": TaskForm()
    }
    return render(request, "model_app/02_form.html", params)


def delete(request):

    if request.method == "POST":
        Task.objects.all().delete()

    return redirect(to="/form")
    

def model(request):

    if request.method == "POST":
        task = NewTask()
        task = NewTaskForm(request.POST, instance=task)
        try:
            task.save()
            msg = "データを登録しました"
        except Exception as e:
            msg = f"データを保存できませんでした。ERROR: {e}"
    else:
        msg = "データを登録してください"

    data = NewTask.objects.all()
    params = {
        "data": data,
        "msg": msg,
        "form": NewTaskForm()
    }
    return render(request, "model_app/03_model.html", params)


def delete_new(request):

    if request.method == "POST":
        NewTask.objects.all().delete()

    return redirect(to="/model")