#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse(u"北京中研软科技有限公司 资产管理系统")
