from django.shortcuts import render
from .forms import SampleForm, DesignForm, ValForm, TypeForm

# Create your views here.

def index(request):
    if request.method == "POST":
        msg = request.POST["msg"]
    else:
        msg = "Default"
    params = {
        "method": request.method,
        "msg": msg
    }
    return render(request, "form_app/01_index.html", params)

def form(request):
    if request.method == "POST":
        msg = request.POST["number"] + ": " + request.POST["text"]
    else:
        msg = "Default"
    params = {
        "method": request.method,
        "msg": msg,
        "form": SampleForm()
    }
    return render(request, "form_app/02_form.html", params)

def design(request):
    if request.method == "POST":
        msg = request.POST["number"] + ": " + request.POST["text"]
    else:
        msg = "Default"
    params = {
        "method": request.method,
        "msg": msg,
        "form": DesignForm()
    }
    return render(request, "form_app/03_design.html", params)

def display(request):
    if request.method == "POST":
        msg = request.POST["number"] + ": " + request.POST["text"]
    else:
        msg = "Default"
    params = {
        "method": request.method,
        "msg": msg,
        "form": DesignForm()
    }
    return render(request, "form_app/04_display.html", params)

def val(request):
    if request.method == "POST":
        msg = request.POST["number"] + ": " + request.POST["text"]
        form = ValForm(request.POST)
        is_valid = form.is_valid
    else:
        msg = "Default"
        form = ValForm()
        is_valid = True
    params = {
        "method": request.method,
        "msg": msg,
        "form": form,
        "is_valid": is_valid
    }
    return render(request, "form_app/05_val.html", params)

def type(request):
    if request.method == "POST":
        msg = request.POST["number"] + ": " + request.POST["text"]
    else:
        msg = "Default"
    params = {
        "method": request.method,
        "msg": msg,
        "form": TypeForm()
    }
    return render(request, "form_app/06_type.html", params)