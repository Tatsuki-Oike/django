from django.shortcuts import render
from django.http import HttpResponse # 追加

# Create your views here.

# 以下を追加
def index(request):
    return HttpResponse("Hello, World")