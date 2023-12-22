from django.shortcuts import render
from django.http import HttpResponse # 追加
from django.views.generic import TemplateView # 追加
import json # 追加

# Create your views here.

# 以下を追加
def index(request):
    if request.method == "POST" or request.method == "PUT" :
        data = json.loads(request.body.decode("utf-8"))
    else:
        data = ""
    response = {
        "method": request.method,
        "query": request.GET,
        "data": data,
    }
    return HttpResponse(json.dumps(response))


class requestClass(TemplateView):
    
    def __init__(self):
        self.response = {
            "method": "",
            "data": {}
        }

    def get(self, request):
        self.response["method"] = request.method
        self.response["data"] = request.GET
        return HttpResponse(json.dumps(self.response))
    
    def post(self, request):
        self.response["method"] = request.method
        self.response["data"] = json.loads(request.body.decode("utf-8"))
        return HttpResponse(json.dumps(self.response))
    
    def put(self, request):
        self.response["method"] = request.method
        self.response["data"] = json.loads(request.body.decode("utf-8"))
        return HttpResponse(json.dumps(self.response))
    
    def delete(self, request):
        self.response["method"] = request.method
        self.response["data"] = request.GET
        return HttpResponse(json.dumps(self.response))
