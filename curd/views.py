from django.shortcuts import render
from django.http import HttpResponse

def hell(request):
    return HttpResponse("hello")