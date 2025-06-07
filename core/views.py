from django.shortcuts import render, redirect
from django.views import View

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

import os
from django.utils import timezone
from dotenv import load_dotenv

from core.products.solar_generators import products
from dadvantech.settings.base import BASE_DIR

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
        email = request.POST.get('email', "")
        first_name = request.POST.get('first_name', "")
        last_name = request.POST.get('last_name', "")
        specialize_groups = ', '.join(request.POST.getlist(
            'specialize_group', []))  # Join checkboxes
        whatsapp = request.POST.get('whatsapp', "")
        volunteer = request.POST.get('volunteer_interest', "")
        preferred_role = request.POST.get('preferred_role', "")
        suggestions = request.POST.get('suggestions', "")
        timestamp = timezone.now().isoformat()

        SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
        SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
        SERVICE_ACCOUNT_FILE = BASE_DIR / "keys.json"

        creds = None
        if os.path.exists(SERVICE_ACCOUNT_FILE):
            creds = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES
            )

        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()

        # Prepare row data to append
        row = [
            timestamp,
            email.lower(),
            first_name.capitalize(),
            last_name.capitalize(),
            specialize_groups,
            whatsapp,
            volunteer,
            preferred_role,
            suggestions
        ]

        # Append the row to the sheet
        try:
            sheet.values().append(
                spreadsheetId=SPREADSHEET_ID,
                range="Community contacts!A1",
                valueInputOption="USER_ENTERED",
                insertDataOption="INSERT_ROWS",
                body={"values": [row]}
            ).execute()
            print("Data appended successfully")
        except Exception as e:
            print(f"Failed to append to sheet: {e}")
        
        GENERAL_GROUP_LINK = os.getenv("GENERAL_GROUP_LINK")

        return redirect(GENERAL_GROUP_LINK)

