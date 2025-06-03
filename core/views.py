from django.shortcuts import render, redirect
from django.views import View

import os
from dotenv import load_dotenv

load_dotenv()

def index(request):
    return render(request, "core/index.html")

def products_in_drive(request):
    url = os.getenv("PRODUCTS_IN_DRIVE_LINK")
    return redirect(url)