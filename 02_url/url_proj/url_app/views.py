from django.shortcuts import render
from django.http import HttpResponse # 追加
import json # 追加

# Create your views here.

# 以下を追加

def index(request):
    return HttpResponse("Hello, World")

def query(request):
    response = {
        "query": request.GET
    }
    return HttpResponse(json.dumps(response))

def param(request, id):
    response = {
        "param": id
    }
    return HttpResponse(json.dumps(response))