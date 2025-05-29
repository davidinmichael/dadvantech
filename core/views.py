from django.shortcuts import render, redirect
from django.views import View


def index(request):
    return render(request, "core/index.html")