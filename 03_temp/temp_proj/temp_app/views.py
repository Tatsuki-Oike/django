from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "temp_app/01_index.html")

def data(request):
    sample_dict = {
        "key1": "value1",
        "key2": "value2"
    }
    return render(request, "temp_app/02_data.html", sample_dict)

def syntax(request):
    sample_dict = {
        "sample_list": [0, 1, 2, 3, 4, 5, 6]
    }
    return render(request, "temp_app/03_syntax.html", sample_dict)

def change(request):
    return render(request, "temp_app/04_change.html")

def design(request):
    return render(request, "temp_app/05_design.html")

def layout(request):
    sample_dict = {
        "key1": "value1",
        "key2": "value2"
    }
    return render(request, "temp_app/06_layout.html", sample_dict)