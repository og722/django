#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("왜 한글 안되냐 또..")
