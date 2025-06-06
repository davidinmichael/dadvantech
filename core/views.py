from django.shortcuts import render, redirect
from django.views import View

import os
from dotenv import load_dotenv

from core.products.solar_generators import products

load_dotenv()

def index(request):
    return render(request, "core/index.html")

def products_in_drive(request):
    url = os.getenv("PRODUCTS_IN_DRIVE_LINK")
    return redirect(url)

def solar_products(request):
    context = {
        "products": products
    }
    return render(request, "core/solars.html", context)


def solar_product(request, pk):
    product = next((item for item in products if item["id"] == pk), None)

    if not product:
        return redirect("products_in_drive")

    context = {
        "product": product
    }
    return render(request, "core/product-details.html", context)

class JoinCommunityView(View):
    def get(self, request):
        return render(request, "core/join_community.html")
    
    def post(self, request):
        return redirect("")
